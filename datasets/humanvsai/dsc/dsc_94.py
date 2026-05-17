def convert_response(allocate_quota_response, project_id):
    status = allocate_quota_response.status
    if status == 'OK':
        return 200, 'Operation successful'
    elif status == 'ERROR':
        return 500, 'Internal server error'
    else:
        return 400, 'Bad request'