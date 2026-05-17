import boto3

def destroy_cloudwatch_log_event(app: str, env: str, region: str) -> bool:
    client = boto3.client('logs', region_name=region)
    log_group_name = f'/aws/lambda/{app}-{env}-'
    response = client.delete_log_group(logGroupName=log_group_name)
    return True
