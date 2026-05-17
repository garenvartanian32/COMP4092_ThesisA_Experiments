def verify_oauth_token_and_set_current_user():
    for func in oauth2._before_request_funcs:
        func()
    if not hasattr(request, 'oauth') or not request.oauth:
        scopes = []
        try:
            valid, req = oauth2.verify_request(scopes)
        except ValueError:
            abort(400, 'Error trying to decode a non urlencoded string.')
        for func in oauth2._after_request_funcs:
            valid, req = func(valid, req)
        if valid:
            request.oauth = req