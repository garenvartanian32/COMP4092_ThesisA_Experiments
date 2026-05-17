import requests
from bs4 import BeautifulSoup

def get_all_distribution_names(url=None):
    if url is None:
        return []

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # This is a very basic example and will likely need to be adjusted based on the actual structure of the webpage
    distribution_names = [tag.text for tag in soup.find_all('h2')]

    return distribution_names