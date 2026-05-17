import boto3

def destroy_cloudwatch_log_event(app='', env='dev', region=''):
    """Destroy Cloudwatch log event.

    Args:
        app (str): Spinnaker Application name.
        env (str): Deployment environment.
        region (str): AWS region.
    Returns:
        bool: True upon successful completion."""

    # Create a boto3 session
    session = boto3.Session(region_name=region)

    # Create a CloudWatch Logs client
    client = session.client('logs')

    # Get the log group name
    log_group_name = '/aws/lambda/' + app

    # Get the log stream names
    response = client.describe_log_streams(logGroupName=log_group_name)
    log_stream_names = [stream['logStreamName'] for stream in response['logStreams']]

    # Delete the log events
    for log_stream_name in log_stream_names:
        client.delete_log_stream(logGroupName=log_group_name, logStreamName=log_stream_name)

    return True