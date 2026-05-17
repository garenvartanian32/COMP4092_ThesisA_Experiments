def encrypt(self, plaintext, iv_bytes=None):
    if not isinstance(plaintext, str):
        raise PlaintextTypeError('Input plaintext must be a string')