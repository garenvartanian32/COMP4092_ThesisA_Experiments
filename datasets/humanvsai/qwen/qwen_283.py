def has_access_api(f):

    def wrapper(*args, **kwargs):
        if not check_permission(f.__name__):
            return ('Unauthorized access', 401)
        return f(*args, **kwargs)
    return wrapper

@has_access_api
def get_user_data(user_id):
    """Retrieve user data for a given user ID."""
    return f'Data for user {user_id}'

def check_permission(permission_name):
    return permission_name == 'get_user_data'