def __get_headers(self, action):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    if action == 'SEARCH':
        headers['X-Search-Action'] = 'true'
    return headers