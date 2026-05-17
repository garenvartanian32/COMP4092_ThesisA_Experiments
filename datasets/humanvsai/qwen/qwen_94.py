def convert_response(allocate_quota_response, project_id):
    if allocate_quota_response.allocate_errors:
        return (400, 'Bad Request: Allocation errors occurred.')
    elif allocate_quota_response.quota_metrics:
        return (200, 'OK: Quota allocation successful.')
    else:
        return (500, 'Internal Server Error: Unexpected response.')