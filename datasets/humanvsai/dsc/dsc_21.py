from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class MyApp:
    def __init__(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.session_factory)

    def create_scoped_session(self, options=None):
        if options is None:
            options = {}
        scopefunc = options.get('scopefunc', None)
        if scopefunc is None:
            from flask import _app_ctx_stack
            scopefunc = _app_ctx_stack().__ident_func
        return scoped_session(self.session_factory, scopefunc=scopefunc)