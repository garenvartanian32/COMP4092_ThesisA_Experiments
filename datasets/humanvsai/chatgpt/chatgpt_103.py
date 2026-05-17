import babel

def auto_format(func):
    locale = babel.default_locale()
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs, locale=locale)
    return wrapper
