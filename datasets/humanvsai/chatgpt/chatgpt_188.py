def ensure_rsa_params(dictionary):
    if 'n' not in dictionary or 'e' not in dictionary or 'd' not in dictionary:
        raise ValueError('Dictionary missing required RSA parameters')
    return dictionary
