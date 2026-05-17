def metadata(self):
    try:
        response = self.client.get_bucket_acl(self.bucket_name)
        acl = response.get('Grants', [])
        owner = response.get('Owner', {})
        return BucketMetadata(acl=acl, owner=owner)
    except Exception as e:
        raise Exception(f'Error retrieving bucket metadata: {e}')