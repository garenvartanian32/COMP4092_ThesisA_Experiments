import requests

def get_catalog_results(self, content_filter_query, query_params=None, traverse_pagination=False):
    base_url = 'http://your-catalog-service.com/search/all'
    headers = {'Content-Type': 'application/json'}

    response = requests.get(base_url, headers=headers, params=content_filter_query)

    if response.status_code == 200:
        data = response.json()

        if traverse_pagination:
            while 'next' in data['links']:
                response = requests.get(data['links']['next'], headers=headers)
                if response.status_code == 200:
                    data['results'].extend(response.json()['results'])
                else:
                    break

        return data
    else:
        return None