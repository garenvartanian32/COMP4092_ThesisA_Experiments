import requests
from bs4 import BeautifulSoup

def get_soundcloud_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1', {'class': 'trackTitle__title'}).text
    artist = soup.find('a', {'class': 'trackUserName'}).text
    plays = soup.find('span', {'class': 'statItem__value'}).text

    return {
        'title': title,
        'artist': artist,
        'plays': plays
    }