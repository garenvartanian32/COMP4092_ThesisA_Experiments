def destroy_cloudwatch_log_event(app='', env='dev', region=''):
    session = boto3.Session(profile_name=env, region_name=region)
    cloudwatch_client = session.client('logs')
    # FIXME: see below
    # TODO: Log group name is required, where do we get it if it is not in application-master-env.json?
    cloudwatch_client.delete_subscription_filter(logGroupName='/aws/lambda/awslimitchecker', filterName=app)
    return True