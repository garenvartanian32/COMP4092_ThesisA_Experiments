def get_all_distribution_names(url=None):
    import requests
    import json
    if url is None:
        url = 'https://pypi.org/pypi/simple/'
    response = requests.get(url)
    if response.status_code == 200:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        distribution_names = [link.get('href').strip('/') for link in links if link.get('href') is not None]
        return distribution_names
    else:
        raise Exception(f'Failed to retrieve data from {url}. Status code: {response.status_code}')