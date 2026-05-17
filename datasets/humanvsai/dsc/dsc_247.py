def create_s3_bucket(bucket_name, bucket_region, bucket_account, template):
    """
    Creates the S3 bucket on the account specified as the destination account for log files

    Args:
        bucket_name (`str`): Name of the S3 bucket
        bucket_region (`str`): AWS Region for the bucket
        bucket_account (:obj:`Account`): Account to create the S3 bucket in
        template (:obj:`Template`): Jinja2 Template object for the bucket policy

    Returns:
        `None`
    """
    # Your code here