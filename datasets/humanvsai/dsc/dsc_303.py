import urllib.parse

def decode(url, charset='utf-8', errors='replace'):
    """Decodes the URL to a tuple made out of strings.  The charset is
        only being used for the path, query and fragment."""

    # Parse the URL
    parsed_url = urllib.parse.urlparse(url)

    # Decode the path, query, and fragment
    decoded_path = urllib.parse.unquote(parsed_url.path, charset, errors)
    decoded_query = urllib.parse.unquote(parsed_url.query, charset, errors)
    decoded_fragment = urllib.parse.unquote(parsed_url.fragment, charset, errors)

    # Return the decoded URL as a tuple
    return (decoded_path, decoded_query, decoded_fragment)