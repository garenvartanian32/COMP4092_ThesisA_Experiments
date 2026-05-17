def _build_url(cls, request, path=None, **changes):
    if path is None:
        path = request.path
    query = request.query.copy()
    for (key, value) in changes.items():
        if value is None:
            continue
        elif value is False:
            query.pop(key, None)
        else:
            query[key] = value
    return request.url.with_path(path).with_query(query)