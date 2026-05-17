def get_versioning_status(self, headers=None):
    response = self.client.get_bucket_versioning(Bucket=self.bucket_name, ExpectedBucketOwner=self.expected_bucket_owner, **headers)
    return response