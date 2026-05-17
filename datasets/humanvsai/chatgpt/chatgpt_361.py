import os
import gzip
import boto3

def compress_and_upload(url: str, local_path: str):
    # Compress local file using gzip compression
    with open(local_path, 'rb') as f_in:
        with gzip.open(local_path + '.gz', 'wb') as f_out:
            f_out.writelines(f_in)

    # Upload compressed file to S3 or Azure Blob Storage
    if url.startswith('s3://'):
        s3 = boto3.client('s3')
        bucket, key = url[5:].split('/', 1)
        s3.upload_file(local_path + '.gz', bucket, key)
    elif url.startswith('wabs://'):
        account_name, container, blob_name = url[7:].split('/', 2)
        block_blob_service = BlockBlobService(account_name=account_name)
        block_blob_service.create_blob_from_path(container, blob_name, local_path + '.gz')

    # Delete compressed file to free up disk space
    os.remove(local_path + '.gz')
