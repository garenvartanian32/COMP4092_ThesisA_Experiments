def validate_tx_order(txs: list) -> int:
    for i in range(len(txs)):
        if txs[i]['sequence'] != i+1:
            return 1
    return 0
