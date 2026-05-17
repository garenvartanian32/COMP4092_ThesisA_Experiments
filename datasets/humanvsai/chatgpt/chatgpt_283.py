from functools import wraps

def permission_required(permission):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check if user has permission
            # If user does not have permission
            # return error message and HTTP 401 status code
            if not user_has_permission(permission):
                return {'error': 'Unauthorized Access'}, 401
            return func(*args, **kwargs)
        return wrapper
    return decorator
