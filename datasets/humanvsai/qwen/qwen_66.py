def query_paths(service_config, endpoint='/paths', retries=3):
    """Query paths from the PFS.

    Send a request to the /paths endpoint of the PFS specified in service_config, and
    retry in case of a failed request if it makes sense."""
    import requests
    import time
    url = f"{service_config['base_url']}{endpoint}"
    headers = {'Authorization': f"Bearer {service_config['token']}"}
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Attempt {attempt + 1} failed: {e}')
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            else:
                raise