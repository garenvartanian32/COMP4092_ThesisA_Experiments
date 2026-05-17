def check_tx(self, tx) -> ResponseCheckTx:
    if not isinstance(tx, Transaction):
        raise TypeError('tx must be an instance of Transaction')
    if tx.id != self.expected_tx_id:
        return ResponseCheckTx(code=1, log='Transaction ID does not match expected ID')
    self.expected_tx_id += 1
    return ResponseCheckTx(code=0, log='Transaction ID matches expected ID')