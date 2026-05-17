from typing import List

class Transaction:
    def __init__(self, id):
        self.id = id

class TransactionPool:
    def __init__(self):
        self.txs = []

    def check_tx(self, tx: Transaction) -> int:
        """Validate the Tx before entry into the mempool
        Checks the txs are submitted in order 1,2,3...
        If not an order, a non-zero code is returned and the tx
        will be dropped."""

        if len(self.txs) == 0:
            self.txs.append(tx)
            return 0

        last_tx = self.txs[-1]
        if tx.id != last_tx.id + 1:
            return 1

        self.txs.append(tx)
        return 0