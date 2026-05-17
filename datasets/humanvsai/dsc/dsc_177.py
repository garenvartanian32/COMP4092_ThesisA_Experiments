def find_credentials(usernames, passwords):
    for username in usernames:
        for password in passwords:
            if check_credentials(username, password):  # Assuming this function exists and returns True if the credentials are valid
                return (username, password)
    return None