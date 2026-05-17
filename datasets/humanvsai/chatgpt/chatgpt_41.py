import requests
from bs4 import BeautifulSoup

def scrape_soundcloud(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    track_data = {}
    track_data['title'] = soup.find('meta', property='og:title')['content']
    track_data['artist'] = soup.find('meta', property='og:audio:artist')['content']
    track_data['genre'] = soup.find('meta', property='soundcloud:genre')['content']
    track_data['description'] = soup.find('meta', property='og:description')['content']
    track_data['artwork_url'] = soup.find('meta', property='og:image')['content']
    track_data['stream_url'] = soup.find('meta', property='og:audio')['content']

    return track_data
