def ensure_rsa_params(jwk_dict, private=False):
    """Ensure all required RSA parameters are present in dictionary"""

    required_params = ['n', 'e']  # 'n' and 'e' are required for public key

    if private:
        required_params.extend(['d', 'p', 'q', 'dp', 'dq', 'qi'])  # 'd', 'p', 'q', 'dp', 'dq', 'qi' are required for private key

    for param in required_params:
        if param not in jwk_dict:
            raise ValueError(f"Missing required parameter: {param}")

    return True