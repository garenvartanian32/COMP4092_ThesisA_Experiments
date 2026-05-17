def update(callback=None, path=None, method=Method.PUT, resource=None, tags=None, summary='Update specified resource.'):

    def decorator(func):
        func._operation = {'callback': callback, 'path': path, 'method': method, 'resource': resource, 'tags': tags, 'summary': summary}
        return func
    return decorator