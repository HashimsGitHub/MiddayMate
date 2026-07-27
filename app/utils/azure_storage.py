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

    # Validate file size (5MB max)
    file.seek(0, 2)  # Seek to end
    file_size = file.tell()
    file.seek(0)  # Seek back to start

    max_size_mb = 5
    if file_size > max_size_mb * 1024 * 1024:
        raise ValueError(f'File too large. Maximum size: {max_size_mb}MB')

    try:
        # Get Azure connection string and container name
        conn_string = current_app.config.get('AZURE_STORAGE_CONNECTION_STRING')
        container_name = current_app.config.get('AZURE_STORAGE_CONTAINER', 'images')

        if not conn_string or conn_string.strip() == '':
            raise ValueError('Azure Storage connection string not configured. Set AZURE_STORAGE_CONNECTION_STRING in .env')

        # Create blob service client
        blob_service_client = BlobServiceClient.from_connection_string(conn_string)
        container_client = blob_service_client.get_container_client(container_name)

        # Generate unique blob name
        ext = file.filename.rsplit('.', 1)[1].lower()
        blob_name = f'{folder}/{uuid.uuid4().hex}.{ext}'

        # Upload to Azure
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(file.stream, overwrite=True)

        # Return public URL
        blob_url = f'https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}'
        return blob_url

    except Exception as e:
        raise ValueError(f'Failed to upload image to Azure: {str(e)}')


def _allowed_file(filename: str, allowed_extensions: set) -> bool:
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
