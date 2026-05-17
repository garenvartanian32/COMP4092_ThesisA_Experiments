import requests

def get_creator_stories(creator_id):
    url = f"https://gateway.marvel.com/v1/public/creators/{creator_id}/stories"
    params = {
        "apikey": YOUR_API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()["data"]
