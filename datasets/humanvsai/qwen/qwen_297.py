def returns(returntype):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, returntype):
                raise TypeError(f'Expected return type {returntype.__name__}, got {type(result).__name__}')
            return result
        return wrapper
    return decorator