import requests

class PaginatedRequest:
    def __init__(self, url):
        self.url = url
        self.next_page = url

    def fetch_next(self):
        if self.next_page is None:
            return None

        response = requests.get(self.next_page)

        # Assuming the next page URL is included in the response headers
        self.next_page = response.headers.get('Next-Page')

        return response.json()