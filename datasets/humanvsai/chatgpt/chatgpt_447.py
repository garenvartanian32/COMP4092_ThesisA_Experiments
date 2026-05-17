import hashlib
import hmac

def sign_message(message, key):
    """
    Signs a message.
    Args:
        message: bytes, Message to be signed.
        key: bytes, Secret key used for the signing operation.
    Returns:
        string, The signature of the message for the given key.
    """
    signature = hmac.new(key, message, hashlib.sha256)
    return signature.hexdigest()
