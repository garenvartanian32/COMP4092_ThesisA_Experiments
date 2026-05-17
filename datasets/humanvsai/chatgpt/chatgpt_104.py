def add_attachments(*file_paths, item_id=None):
    """
    Add attachments using filenames as title

    Arguments:
    - file_paths: One or more file paths to add as attachments
    - item_id: An optional Item ID, which will create child attachments
    """

    # Import necessary libraries
    import os
    import requests
    from requests.exceptions import HTTPError

    # Set the URL to the API endpoint for creating attachments
    url = 'https://my_api_endpoint.com/attachments'

    # Iterate over the file paths
    for file_path in file_paths:

        # Get the filename from the path
        file_name = os.path.basename(file_path)

        # Open the file in binary mode
        with open(file_path, 'rb') as file:

            # Set the data and headers for the API request
            data = {'name': file_name}
            files = {'file': file}
            headers = {'content-type': 'multipart/form-data'}
            if item_id:
                data['parent'] = item_id

            # Send the API request
            try:
                response = requests.post(url, data=data, files=files, headers=headers)
                response.raise_for_status()
                print(f'Successfully added attachment: "{file_name}"')
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')
