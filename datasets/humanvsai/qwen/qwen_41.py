def get_soundcloud_data(url):
    import requests
    from bs4 import BeautifulSoup
    import re
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f'Failed to retrieve the page. Status code: {response.status_code}')
    soup = BeautifulSoup(response.text, 'html.parser')
    json_data = soup.find('script', type='application/ld+json')
    if not json_data:
        raise ValueError('Could not find JSON data in the page')
    import json
    data = json.loads(json_data.string)
    audio_data = {'title': data.get('name', 'Unknown Title'), 'artist': data.get('author', {}).get('name', 'Unknown Artist'), 'duration': data.get('duration', 'Unknown Duration'), 'description': data.get('description', 'No Description Available'), 'url': data.get('url', 'No URL Available')}
    return audio_data
url = 'https://soundcloud.com/user-123456789/track-name'
audio_data = get_soundcloud_data(url)