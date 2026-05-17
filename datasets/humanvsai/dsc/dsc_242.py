import boto3
from botocore.exceptions import BotoCoreError

class Bucket:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3 = boto3.resource('s3')

    def metadata(self):
        try:
            bucket_metadata = self.s3.Bucket(self.bucket_name)
            return bucket_metadata
        except BotoCoreError as e:
            raise Exception(f"Error retrieving bucket metadata: {e}")