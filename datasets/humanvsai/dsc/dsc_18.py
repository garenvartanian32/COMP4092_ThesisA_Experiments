def check(self, var):
    """Return True if the variable matches this type, and False otherwise."""
    return isinstance(var, self)