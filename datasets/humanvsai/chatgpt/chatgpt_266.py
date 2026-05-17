def wrapped_method(original_func):
    def wrapper(*args, queued=False, isgroup=False, **kwargs):
        # Do something with `queued` and `isgroup` parameters
        return original_func(*args, **kwargs)
    return wrapper
