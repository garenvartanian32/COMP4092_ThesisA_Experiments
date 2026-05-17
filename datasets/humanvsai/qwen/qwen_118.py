def _raise_response_exceptions(response):
    if response.status_code == 400:
        raise ValueError('Bad Request')
    elif response.status_code == 401:
        raise PermissionError('Unauthorized')
    elif response.status_code == 403:
        raise PermissionError('Forbidden')
    elif response.status_code == 404:
        raise FileNotFoundError('Not Found')
    elif response.status_code == 500:
        raise RuntimeError('Internal Server Error')
    elif response.status_code == 502:
        raise ConnectionError('Bad Gateway')
    elif response.status_code == 503:
        raise ConnectionError('Service Unavailable')
    elif response.status_code == 504:
        raise ConnectionError('Gateway Timeout')
    else:
        response.raise_for_status()

def fetch_data(url):
    """Fetch data from a URL and handle exceptions."""
    import requests
    try:
        response = requests.get(url)
        _raise_response_exceptions(response)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')
        raise