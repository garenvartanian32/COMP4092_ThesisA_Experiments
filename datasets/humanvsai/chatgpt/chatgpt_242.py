def retrieve_bucket_metadata(bucket_name):
    try:
        bucket_metadata = bucket.BucketMetadata(bucket_name)
        # Retrieve the metadata about the bucket
        # ...
        return bucket_metadata
    except Exception:
        raise Exception('Error retrieving bucket metadata')
