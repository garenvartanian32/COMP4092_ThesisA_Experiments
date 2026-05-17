import requests
import time

def query_paths(service_config, retry_attempts=3, retry_delay=5):
    url = service_config['pfs_endpoint'] + '/paths'
    for count in range(retry_attempts+1):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f'Failed to get response. Status code: {response.status_code}')
        except Exception as e:
            print(f'Error occurred: {e}. Retrying attempt {count+1}/{retry_attempts+1} after {retry_delay} seconds.')
            time.sleep(retry_delay)
    raise Exception(f'Failed to get response from {url} after {retry_attempts} attempts.')
