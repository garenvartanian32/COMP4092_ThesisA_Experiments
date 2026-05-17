def find_status(response):
    if 'status' in response.json():
        return response.json()['status']
    else:
        return 'None'
