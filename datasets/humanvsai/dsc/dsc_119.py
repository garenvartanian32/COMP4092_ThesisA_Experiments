import requests

class Creator:
    def __init__(self, creator_id):
        self.creator_id = creator_id

    def get_stories(self):
        url = f"https://api.example.com/creators/{self.creator_id}/stories"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None