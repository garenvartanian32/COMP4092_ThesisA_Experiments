def find_credentials():
    for username in ['admin', 'user', 'test']:
        for password in ['123456', 'password', 'letmein']:
            if check_credentials(username, password):
                return (username, password)
    return None

def check_credentials(username, password):
    """Check if the given username and password are correct"""
    return username == 'admin' and password == 'password'
credentials = find_credentials()