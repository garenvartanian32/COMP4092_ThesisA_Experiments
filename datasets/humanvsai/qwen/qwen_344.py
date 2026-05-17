def build_swagger_spec(user, repo, sha, serverName):
    grlc_api_url = f'https://grlc.io/api/{user}/{repo}/swagger.json'
    response = requests.get(grlc_api_url)
    if response.status_code == 200:
        swagger_spec = response.json()
        swagger_spec['servers'] = [{'url': f'https://{serverName}/api/{user}/{repo}'}]
        return swagger_spec
    else:
        raise Exception(f'Failed to fetch swagger specification from {grlc_api_url}')
user = 'exampleUser'
repo = 'exampleRepo'
sha = 'exampleSha'
serverName = 'exampleServerName'
swagger_spec = build_swagger_spec(user, repo, sha, serverName)