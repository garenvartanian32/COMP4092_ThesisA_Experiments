def get_intro_prompt(self):
    try:
        response = requests.get('https://psiturk.org/status')
        if response.status_code == 200:
            return response.text
        else:
            return 'Failed to retrieve system status message.'
    except requests.exceptions.RequestException as e:
        return f'An error occurred: {e}'