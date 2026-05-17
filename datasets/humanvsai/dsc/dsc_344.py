import requests
import json

def build_swagger_spec(user, repo, sha, serverName):
    """Build grlc specification for the given github user / repo in swagger format"""

    # Construct the URL to the raw swagger.json file
    url = f"https://raw.githubusercontent.com/{user}/{repo}/{sha}/swagger.json"

    # Make a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Load the JSON data from the response
        data = json.loads(response.text)

        # Update the server name
        data["servers"] = [{"url": serverName}]

        # Return the updated Swagger specification
        return data
    else:
        # If the request was not successful, return an error message
        return f"Failed to fetch swagger.json from {url}. Status code: {response.status_code}"