def create_s3_bucket(cls, bucket_name, bucket_region, bucket_account, template):
        s3 = get_aws_session(bucket_account).client('s3', region_name=bucket_region)
        # Check to see if the bucket already exists and if we have access to it
        try:
            s3.head_bucket(Bucket=bucket_name)
        except ClientError as ex:
            status_code = ex.response['ResponseMetadata']['HTTPStatusCode']
            # Bucket exists and we do not have access
            if status_code == 403:
                raise Exception('Bucket {} already exists but we do not have access to it and so cannot continue'.format(
                    bucket_name
                ))
            # Bucket does not exist, lets create one
            elif status_code == 404:
                try:
                    s3.create_bucket(
                        Bucket=bucket_name,
                        CreateBucketConfiguration={
                            'LocationConstraint': bucket_region
                        }
                    )
                    auditlog(
                        event='cloudtrail.create_s3_bucket',
                        actor=cls.ns,
                        data={
                            'account': bucket_account.account_name,
                            'bucket_region': bucket_region,
                            'bucket_name': bucket_name
                        }
                    )
                except Exception:
                    raise Exception('An error occured while trying to create the bucket, cannot continue')
        try:
            bucket_acl = template.render(
                bucket_name=bucket_name,
                account_id=bucket_account.account_number
            )
            s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_acl)
        except Exception as ex:
            raise Warning('An error occurred while setting bucket policy: {}'.format(ex))