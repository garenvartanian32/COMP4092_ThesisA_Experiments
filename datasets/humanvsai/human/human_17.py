def get_all_distribution_names(url=None):
    if url is None:
        url = DEFAULT_INDEX
    client = ServerProxy(url, timeout=3.0)
    return client.list_packages()