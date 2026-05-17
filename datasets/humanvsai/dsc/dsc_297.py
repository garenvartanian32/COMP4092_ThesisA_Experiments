def check_return_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, returntype):
            raise TypeError(f"Expected return type {returntype}, but got {type(result)}")
        return result
    return wrapper

def returns(returntype):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, returntype):
                raise TypeError(f"Expected return type {returntype}, but got {type(result)}")
            return result
        return wrapper
    return decorator