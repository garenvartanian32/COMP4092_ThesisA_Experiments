def __get_headers(self, action):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    if action == 'GET':
        headers['X-Custom-Header'] = 'value'  # Add custom headers as needed
    elif action == 'PUT':
        headers['X-Custom-Header'] = 'value'  # Add custom headers as needed
    elif action == 'DELETE':
        headers['X-Custom-Header'] = 'value'  # Add custom headers as needed
    elif action == 'SEARCH':
        headers['X-Custom-Header'] = 'value'  # Add custom headers as needed
    else:
        raise ValueError(f"Unknown action: {action}")

    return headers