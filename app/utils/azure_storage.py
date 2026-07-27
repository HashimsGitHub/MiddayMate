"""Azure Blob Storage utilities for image uploads."""

import os
import uuid
from flask import current_app
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta


def upload_image_to_azure(file, folder: str = 'vendors') -> str:
    """
    Upload an image file to Azure Blob Storage.

    Args:
        file: File object from Flask request
        folder: Folder path in container (vendors, venues, users, etc.)

    Returns:
        str: Public URL of the uploaded blob

    Raises:
        ValueError: If file is invalid or upload fails
    """
    if not file or file.filename == '':
        raise ValueError('No file provided')

    # Validate file type
    allowed_extensions = {'jpg', 'jpeg', 'png', 'webp', 'gif'}
    if not _allowed_file(file.filename, allowed_extensions):
        raise ValueError(f'Invalid file type. Allowed: {", ".join(allowed_extensions)}')

    try:
        # Get Azure connection string and container name
        conn_string = current_app.config.get('AZURE_STORAGE_CONNECTION_STRING')
        container_name = current_app.config.get('AZURE_STORAGE_CONTAINER', 'images')

        print(f"\n[AZURE UPLOAD] Starting upload process...")
        print(f"[AZURE UPLOAD] Connection string present: {bool(conn_string)}")
        print(f"[AZURE UPLOAD] Container name: {container_name}")

        if not conn_string or conn_string.strip() == '':
            raise ValueError('Azure Storage connection string not configured. Set AZURE_STORAGE_CONNECTION_STRING in .env')

        print(f"[AZURE UPLOAD] Reading file: {file.filename}")
        # Read file content
        file.seek(0)
        file_content = file.read()
        print(f"[AZURE UPLOAD] File size: {len(file_content)} bytes")

        # Validate file size (5MB max)
        max_size_mb = 5
        if len(file_content) > max_size_mb * 1024 * 1024:
            raise ValueError(f'File too large. Maximum size: {max_size_mb}MB')

        print(f"[AZURE UPLOAD] Creating BlobServiceClient...")
        # Create blob service client
        blob_service_client = BlobServiceClient.from_connection_string(conn_string)
        print(f"[AZURE UPLOAD] ✓ Created service client")

        print(f"[AZURE UPLOAD] Getting container client for '{container_name}'...")
        container_client = blob_service_client.get_container_client(container_name)
        print(f"[AZURE UPLOAD] ✓ Got container client")

        # Generate unique blob name
        ext = file.filename.rsplit('.', 1)[1].lower()
        blob_name = f'{folder}/{uuid.uuid4().hex}.{ext}'
        print(f"[AZURE UPLOAD] Generated blob name: {blob_name}")

        # Upload to Azure
        print(f"[AZURE UPLOAD] Uploading blob...")
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(file_content, overwrite=True)
        print(f"[AZURE UPLOAD] ✓ Blob uploaded successfully")

        # Return public URL
        blob_url = f'https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}'
        print(f"[AZURE UPLOAD] ✓ Generated URL: {blob_url}")
        return blob_url

    except Exception as e:
        print(f"[AZURE UPLOAD] ✗ ERROR: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        raise ValueError(f'Failed to upload image to Azure: {str(e)}')


def _allowed_file(filename: str, allowed_extensions: set) -> bool:
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
