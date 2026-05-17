def validate_client_key(client_key):
    # validate the client key here
    if len(client_key) == 32:
        return True
    else:
        return False
