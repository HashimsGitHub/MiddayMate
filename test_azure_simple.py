#!/usr/bin/env python3
"""Simple Azure Blob test using exact connection string from Flask app"""

from dotenv import load_dotenv
import os
from azure.storage.blob import BlobServiceClient

# Load .env
load_dotenv()

conn_string = os.environ.get('AZURE_STORAGE_CONNECTION_STRING')
container_name = os.environ.get('AZURE_STORAGE_CONTAINER', 'images')

print(f"Account Name: middaymatesa")
print(f"Container: {container_name}")
print(f"Connection String Present: {bool(conn_string)}")
print()

# Step 1: Connect
try:
    print("Step 1: Creating BlobServiceClient...")
    blob_service_client = BlobServiceClient.from_connection_string(conn_string)
    print("✓ Connected to Azure account")
except Exception as e:
    print(f"✗ Failed to connect: {e}")
    exit(1)

# Step 2: Get container
try:
    print(f"\nStep 2: Getting container '{container_name}'...")
    container_client = blob_service_client.get_container_client(container_name)
    print("✓ Got container client")
except Exception as e:
    print(f"✗ Failed to get container: {e}")
    exit(1)

# Step 3: List blobs to verify container exists
try:
    print(f"\nStep 3: Listing blobs in container...")
    blobs = list(container_client.list_blobs())
    print(f"✓ Container exists! Found {len(blobs)} blobs")
    for blob in blobs[:3]:  # Show first 3
        print(f"  - {blob.name}")
except Exception as e:
    print(f"✗ Container doesn't exist or can't access: {e}")
    exit(1)

# Step 4: Try uploading test file
try:
    print(f"\nStep 4: Uploading test file...")
    test_blob = container_client.get_blob_client('test-connection.txt')
    test_blob.upload_blob(b'Test connection successful', overwrite=True)
    print("✓ Test file uploaded successfully!")
except Exception as e:
    print(f"✗ Failed to upload: {e}")
    exit(1)

print("\n" + "="*50)
print("✅ All tests passed! Azure Blob Storage works!")
print("="*50)
