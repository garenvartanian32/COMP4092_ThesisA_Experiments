def encrypt(self, plaintext, iv_bytes=None):
        if not isinstance(plaintext, str):
            raise PlaintextTypeError("Input plaintext is not of type string")
        if iv_bytes is None:
            iv_bytes = fte.bit_ops.random_bytes(Encrypter._IV_LENGTH)
        iv1_bytes = '\x01' + iv_bytes
        iv2_bytes = '\x02' + iv_bytes
        W1 = iv1_bytes
        W1 += fte.bit_ops.long_to_bytes(
            len(plaintext), Encrypter._MSG_COUNTER_LENGTH)
        W1 = self._ecb_enc_K1.encrypt(W1)
        counter_length_in_bits = AES.block_size * 8
        counter_val = fte.bit_ops.bytes_to_long(iv2_bytes)
        counter = Counter.new(
            counter_length_in_bits, initial_value=counter_val)
        ctr_enc = AES.new(key=self.K1,
                          mode=AES.MODE_CTR,
                          IV='\x00' * 8 + iv2_bytes,
                          counter=counter)
        W2 = ctr_enc.encrypt(plaintext)
        mac = HMAC.new(self.K2, W1 + W2, SHA512)
        T = mac.digest()
        T = T[:Encrypter._MAC_LENGTH]
        ciphertext = W1 + W2 + T
        return ciphertext