def copy_func(f, name=None, sinceversion=None, doc=None):
    """
    Returns a function with same code, globals, defaults, closure, and
    name (or provide a new name).
    """
    # See
    # http://stackoverflow.com/questions/6527633/how-can-i-make-a-deepcopy-of-a-function-in-python
    fn = types.FunctionType(f.__code__, f.__globals__, name or f.__name__, f.__defaults__,
                            f.__closure__)
    # in case f was given attrs (note this dict is a shallow copy):
    fn.__dict__.update(f.__dict__)
    if doc is not None:
        fn.__doc__ = doc
    if sinceversion is not None:
        fn = since(sinceversion)(fn)
    return fn