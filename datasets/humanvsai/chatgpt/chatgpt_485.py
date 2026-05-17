def create_http_headers(action):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    
    if action == 'GET':
        headers['Accept'] = 'application/json'
    elif action == 'PUT' or action == 'DELETE':
        headers['Content-Type'] = 'application/json'
    elif action == 'SEARCH':
        headers['Accept'] = 'application/json'
        headers['Content-Type'] = 'application/json'

    return headers
