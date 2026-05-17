def destroy_cloudwatch_log_event(app='', env='dev', region=''):
    import boto3
    client = boto3.client('logs', region_name=region)
    log_group_name = f'/aws/lambda/{app}-{env}'
    try:
        response = client.delete_log_group(logGroupName=log_group_name)
        print(f'Log group {log_group_name} deleted successfully.')
        return True
    except client.exceptions.ResourceNotFoundException:
        print(f'Log group {log_group_name} not found.')
        return False
    except Exception as e:
        print(f'An error occurred: {e}')
        return False