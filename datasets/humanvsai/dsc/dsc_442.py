def _get_header(self):
    """Gets header of table

    :return: markdown-formatted header"""

    # Assuming you have a list of headers
    headers = ['Header 1', 'Header 2', 'Header 3']

    # Create a markdown-formatted header
    header_str = '| ' + ' | '.join(headers) + ' |'

    return header_str