import requests

class FeedSubscriber:
    def __init__(self):
        self.subscriptions = []

    def subscribe(self, feedUrl):
        """Adds a feed to the top-level subscription list

        Ubscribing seems idempotent, you can subscribe multiple times
        without error

        returns True or throws HTTPError"""

        # Check if the feed is already subscribed
        if feedUrl in self.subscriptions:
            return True

        # Try to subscribe to the feed
        try:
            response = requests.get(feedUrl)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise err

        # If successful, add the feed to the subscriptions
        self.subscriptions.append(feedUrl)
        return True