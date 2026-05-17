import collections

def _merge_headers(self, call_specific_headers=None):
    # Get headers from the connection object
    connection_headers = self.connection.headers

    # Convert headers to a case-insensitive dictionary
    connection_headers = {k.lower(): v for k, v in connection_headers.items()}

    # Merge headers from different sources
    merged_headers = collections.ChainMap(call_specific_headers or {}, connection_headers)

    return merged_headers