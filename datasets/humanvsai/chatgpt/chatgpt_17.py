import requests

def get_distribution_names(url):
    response = requests.get(url)
    json_response = response.json()
    distributions = json_response['distributions']
    return [dist['name'] for dist in distributions]
