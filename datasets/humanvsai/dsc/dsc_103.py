import babel.numbers
import locale

def _wrap_locale_formatter(fn, locale_type):
    """Wrap a Babel data formatting function to automatically format
    for currently installed locale."""
    # Get the current locale
    current_locale = locale.getdefaultlocale()[0]

    # Set the locale
    locale.setlocale(locale_type, current_locale)

    # Wrap the function
    def wrapped_fn(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapped_fn