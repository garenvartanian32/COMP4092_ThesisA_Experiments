import requests

def _get_async_status(self, response):
    """Attempt to find status info in response body.

    :param requests.Response response: latest REST call response.
    :rtype: str
    :returns: Status if found, else 'None'."""

    # Assuming the status is in the response body as a JSON object
    try:
        response_json = response.json()
        if 'status' in response_json:
            return response_json['status']
        else:
            return 'None'
    except ValueError:
        return 'None'