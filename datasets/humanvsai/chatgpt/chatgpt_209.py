import requests

def add_feed_to_subscription_list(feed_url: str) -> bool:
    headers = {'Content-Type': 'application/json'}
    payload = {'url': feed_url}
    response = requests.post('https://example.com/subscription', headers=headers, json=payload)

    if response.ok:
        return True
    else:
        response.raise_for_status()
