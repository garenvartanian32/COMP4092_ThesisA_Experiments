def _wrap_deprecated_function(func, message):
    """ Wrap the deprecated function to print out deprecation warnings"""
    def _(col):
        warnings.warn(message, DeprecationWarning)
        return func(col)
    return functools.wraps(func)(_)