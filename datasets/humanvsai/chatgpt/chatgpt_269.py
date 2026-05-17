import slack_sdk
import os

def unarchive_channel(channel:str):
    client = slack_sdk.WebClient(token=os.environ['SLACK_BOT_TOKEN'])
    response = client.conversations_unarchive(channel=channel)
    return response
