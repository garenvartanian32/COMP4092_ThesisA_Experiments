def request(self, method, url, *args, **kwargs):
    response = self.session.request(method, url, *args, **kwargs)
    response.raise_for_status()
    return response.json()