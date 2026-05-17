import requests
    
def build_grlc_specification(github_user, github_repo):
    grlc_url = f'https://grlc.io/api/v1/spec/github/{github_user}/{github_repo}'
    response = requests.get(grlc_url)
    specification = response.json()
    return specification
