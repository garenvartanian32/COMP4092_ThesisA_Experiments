def ensure_rsa_params(jwk_dict, private):
    required_keys = ['n', 'e'] if not private else ['n', 'e', 'd', 'p', 'q', 'dp', 'dq', 'qi']
    for key in required_keys:
        if key not in jwk_dict:
            raise ValueError(f'Missing required RSA parameter: {key}')
    return jwk_dict
jwk_dict = {'n': 'some_value', 'e': 'some_value', 'd': 'some_value', 'p': 'some_value', 'q': 'some_value', 'dp': 'some_value', 'dq': 'some_value', 'qi': 'some_value'}