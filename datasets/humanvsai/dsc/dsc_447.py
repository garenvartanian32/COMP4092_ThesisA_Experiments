import rsa

def sign(message, private_key):
    """Signs a message.

    Args:
        message: bytes, Message to be signed.
        private_key: rsa.PrivateKey, Private key to sign the message.

    Returns:
        string, The signature of the message for the given key.
    """
    return rsa.sign(message, private_key, 'SHA-1')