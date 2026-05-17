def get_catalog_results(self, content_filter_query, query_params=None, traverse_pagination=False):
    if query_params is None:
        query_params = {}
    full_query_params = {**content_filter_query, **query_params}
    response = self.make_request('GET', '/search/all', params=full_query_params)
    if traverse_pagination:
        all_results = response['results']
        while 'next' in response and response['next']:
            next_url = response['next']
            response = self.make_request('GET', next_url, params=full_query_params)
            all_results.extend(response['results'])
        return {'results': all_results}
    else:
        return response