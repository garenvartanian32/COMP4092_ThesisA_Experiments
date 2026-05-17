def _wrap_locale_formatter(fn, locale_type):

    def wrapper(*args, **kwargs):
        locale = get_current_locale()
        return fn(locale, *args, **kwargs)
    return wrapper

def get_current_locale():
    """Retrieve the current locale from the context."""
    return 'en_US'
from babel.dates import format_datetime
from babel.numbers import format_currency
format_datetime = _wrap_locale_formatter(format_datetime, 'date')
format_currency = _wrap_locale_formatter(format_currency, 'currency')