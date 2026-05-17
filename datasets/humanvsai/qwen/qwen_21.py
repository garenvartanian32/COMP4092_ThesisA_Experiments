def create_scoped_session(self, options=None):
    if options is None:
        options = {}
    scopefunc = options.pop('scopefunc', None)
    if scopefunc is None:
        scopefunc = _app_ctx_stack.__ident_func__
    session_factory = self.create_session(options)
    return scoped_session(session_factory, scopefunc=scopefunc)