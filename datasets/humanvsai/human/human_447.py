def sign(self, message):
        message = _helpers._to_bytes(message, encoding='utf-8')
        return rsa.pkcs1.sign(message, self._key, 'SHA-256')