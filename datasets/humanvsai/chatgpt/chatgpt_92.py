import boto3

def get_bucket_versioning_status(bucket_name: str) -> dict:
    """
    Returns the current status of versioning on the bucket.
    :rtype: dict
    :returns: A dictionary containing a key named 'Versioning'
              that can have a value of either Enabled, Disabled,
              or Suspended. Also, if MFADelete has ever been enabled
              on the bucket, the dictionary will contain a key
              named 'MFADelete' which will have a value of either
              Enabled or Suspended.
    """
    s3 = boto3.client('s3')
    
    try:
        response = s3.get_bucket_versioning(Bucket=bucket_name)
    except:
        return {'Versioning': 'Error'}
    
    version_status = response.get('Status', 'Disabled')
    mfa_status = response.get('MFADelete', 'Not configured')
    
    result = {'Versioning': version_status}
    
    if mfa_status != 'Not configured':
        result['MFADelete'] = mfa_status
    
    return result
