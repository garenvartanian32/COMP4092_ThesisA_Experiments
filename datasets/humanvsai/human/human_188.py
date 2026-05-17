def ensure_rsa_params(jwk_dict, private):
    provided = frozenset(jwk_dict.keys())
    if private is not None and private:
        required = RSA_PUBLIC_REQUIRED | RSA_PRIVATE_REQUIRED
    else:
        required = RSA_PUBLIC_REQUIRED
    return ensure_params('RSA', provided, required)