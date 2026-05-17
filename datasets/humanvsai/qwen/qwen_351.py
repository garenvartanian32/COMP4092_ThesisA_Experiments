def update(self, status, source=None, params={}):
    if source is None:
        source = self.source
    if not params:
        params = {}
    params.update({'status': status, 'source': source})
    return self.api_call('statuses/update', params)