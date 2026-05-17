import requests

def make_api_request(url):
    response = requests.get(url)
    return response
