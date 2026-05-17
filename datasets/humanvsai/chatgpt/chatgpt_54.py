def search_all_results(content_filter_query, query_params, traverse_pagination=False):
    url = 'https://discovery-service.com/search/all'

    if not traverse_pagination:
        response = requests.get(url, params={**content_filter_query, **query_params})
        return response.json()
    else:
        records = []
        while True:
            response = requests.get(url, params={**content_filter_query, **query_params})
            records.extend(response.json()['results'])
            if not response.json()['next_page']:
                break
            else:
                query_params['page'] = response.json()['next_page']
        return records
