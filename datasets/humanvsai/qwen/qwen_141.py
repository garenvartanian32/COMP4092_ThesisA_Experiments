def _get_async_status(self, response):
    try:
        response_json = response.json()
        status = response_json.get('status', 'None')
        return status
    except ValueError:
        return 'None'
    except AttributeError:
        return 'None'