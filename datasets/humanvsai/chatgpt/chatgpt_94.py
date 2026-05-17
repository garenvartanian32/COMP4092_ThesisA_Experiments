def compute_http_status(allocate_quota_response):
    code = allocate_quota_response.response_code
    message = allocate_quota_response.service_data.allocate_quota_response_v1.error_message
    return (code, message)
