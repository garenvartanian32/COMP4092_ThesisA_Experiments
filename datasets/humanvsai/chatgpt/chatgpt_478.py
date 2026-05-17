import requests

def intro_prompt():
    try:
        response = requests.get('http://www.psiturk.org')
        if response.status_code == 200:
            status_message = requests.get('http://www.psiturk.org/status').text
            print(f'Welcome to the network-aware version of the intro prompt. System status: {status_message}')
    except:
        print('Welcome to the intro prompt')
