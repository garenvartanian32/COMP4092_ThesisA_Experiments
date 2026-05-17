from urllib.parse import urlencode, urlparse, urlunparse

def _build_url(cls, request, path=None, **changes):
    # Parse the original URL
    parsed_url = urlparse(request.url)

    # Get the original queries
    original_queries = dict(qc.split("=") for qc in parsed_url.query.split("&"))

    # Update the original queries with the changes
    for key, value in changes.items():
        if value is False:
            original_queries.pop(key, None)  # Remove the key if it exists
        elif value is not None:
            original_queries[key] = value  # Update the key with the new value

    # Build the new URL
    new_url = urlunparse((
        parsed_url.scheme,
        parsed_url.netloc,
        path or parsed_url.path,
        "",  # This should be empty for the queries
        urlencode(original_queries, doseq=True),  # Encode the queries
        ""  # Fragment is not used
    ))

    return new_url