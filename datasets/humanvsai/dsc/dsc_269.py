import requests

def channels_unarchive(self, *, channel: str):
    """Unarchives a channel.

    Args:
        channel (str): The channel id. e.g. 'C1234567890'
    """
    url = "https://slack.com/api/channels.unarchive"
    headers = {
        "Authorization": "Bearer YOUR_SLACK_API_TOKEN",
        "Content-Type": "application/json; charset=utf-8"
    }
    data = {
        "channel": channel
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Channel unarchived successfully.")
    else:
        print("Failed to unarchive channel. Error: ", response.text)