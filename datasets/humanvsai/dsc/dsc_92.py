import boto3

def get_versioning_status(bucket_name):
    s3 = boto3.resource('s3')
    bucket_versioning = s3.BucketVersioning(bucket_name)

    response = {
        'Versioning': bucket_versioning.status,
        'MFADelete': bucket_versioning.mfa_delete
    }

    return response