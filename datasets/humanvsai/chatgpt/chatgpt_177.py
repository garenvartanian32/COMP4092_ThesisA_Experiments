def try_credentials(credentials_list, validate_function):
    for credentials in credentials_list:
        if validate_function(credentials):
            return credentials
    return None
