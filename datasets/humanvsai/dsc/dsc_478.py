import requests

def get_intro_prompt(self):
    try:
        response = requests.get('http://psiTurk.org')
        if response.status_code == 200:
            return "You can reach psiTurk.org"
        else:
            return "You can't reach psiTurk.org"
    except requests.ConnectionError:
        return "You can't reach psiTurk.org"