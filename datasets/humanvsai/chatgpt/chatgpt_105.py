import hmac
import hashlib

class PlaintextTypeError(Exception):
    pass

class AuthenticatedEncryption:
    def __init__(self, key):
        self.key = key
    
    def _generate_key(self, data):
        return hmac.new(self.key, data, hashlib.sha256).digest()
    
    def encrypt(self, plaintext):
        if not isinstance(plaintext, str):
            raise PlaintextTypeError("Plaintext should be a string")
        
        key = self._generate_key(plaintext.encode())
        ciphertext = hmac.new(key, plaintext.encode(), hashlib.sha256).hexdigest()
        
        return ciphertext.encode() + key
