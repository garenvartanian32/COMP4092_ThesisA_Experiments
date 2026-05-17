from sqlalchemy.orm import scoped_session

def create_scoped_session(create_session, **options):
    scopefunc = options.pop('scopefunc', None)
    return scoped_session(create_session, scopefunc=scopefunc, **options)
