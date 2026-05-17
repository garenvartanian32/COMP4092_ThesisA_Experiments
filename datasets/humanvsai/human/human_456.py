def check_tx(self, tx) -> ResponseCheckTx:
        value = decode_number(tx)
        if not value == (self.txCount + 1):
            # respond with non-zero code
            return ResponseCheckTx(code=1)
        return ResponseCheckTx(code=CodeTypeOk)