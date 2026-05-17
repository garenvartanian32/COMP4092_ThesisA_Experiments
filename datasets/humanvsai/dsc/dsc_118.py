def _raise_response_exceptions(response):
    """Raise specific errors on some status codes."""
    if response.status_code == 400:
        raise ValueError("Bad request")
    elif response.status_code == 404:
        raise FileNotFoundError("Not found")
    elif response.status_code == 500:
        raise ConnectionError("Internal server error")
    # Add more status codes and exceptions as needed