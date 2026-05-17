def ensure_single_role(user_roles):
    roles_count = len(user_roles)
    if roles_count == 0:
        raise Exception('User has no roles')
    elif roles_count > 1:
        raise Exception('User has multiple roles')
    elif 'prison-clerk' in user_roles and 'prison' not in user_roles:
        raise Exception('User in prison-clerk role but not assigned to prison')
    else:
        return True
