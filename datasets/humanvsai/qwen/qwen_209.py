def subscribe(self, feedUrl):
    try:
        response = self.session.post(self.base_url + '/subscribe', data={'feedUrl': feedUrl})
        response.raise_for_status()
        return True
    except requests.exceptions.HTTPError as e:
        raise e

def unsubscribe(self, feedUrl):
    """Removes a feed from the top-level subscription list

        Unsubscribing seems idempotent, you can unsubscribe multiple times
        without error

        returns True or throws HTTPError"""
    try:
        response = self.session.post(self.base_url + '/unsubscribe', data={'feedUrl': feedUrl})
        response.raise_for_status()
        return True
    except requests.exceptions.HTTPError as e:
        raise e

def list_subscriptions(self):
    """Lists all feeds in the top-level subscription list

        returns a list of feed URLs or throws HTTPError"""
    try:
        response = self.session.get(self.base_url + '/subscriptions')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        raise e

def get_feed(self, feedUrl):
    """Fetches the latest entries from a specific feed

        returns a list of feed entries or throws HTTPError"""
    try:
        response = self.session.get(self.base_url + '/feed', params={'feedUrl': feedUrl})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        raise e