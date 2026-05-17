import boto3

def create_s3_bucket(bucket_name, bucket_region, bucket_account, template):
    # Creating a client to communicate with AWS S3
    s3_client = boto3.client('s3')
    # Creating an S3 Bucket in the destination account
    s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': bucket_region})
    # Configuring S3 Bucket policies
    bucket_policy = template.render(bucket_name=bucket_name, bucket_account=bucket_account)
    s3_client.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
