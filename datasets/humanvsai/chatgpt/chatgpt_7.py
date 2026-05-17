def build_response_url(original_url, change_queries):
    parsed_url = urlparse(original_url)
    queries = dict(parse_qsl(parsed_url.query))
    for query_key, query_value in change_queries.items():
        if query_value is None:
            queries.pop(query_key, None)
        else:
            queries[query_key] = query_value if query_value != False else ''
    new_query_string = urlencode(queries, doseq=True)
    return urlunparse(parsed_url._replace(query=new_query_string))
