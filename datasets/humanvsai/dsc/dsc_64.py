import requests

def request(self, method, url, *args, **kwargs):
    """Make a request to the Ansible Tower API, and return the response."""
    response = requests.request(method, url, *args, **kwargs)
    return response