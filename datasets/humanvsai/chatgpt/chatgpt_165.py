def add_transaction_to_log_and_merkle_tree(log, merkle_tree, transaction):
    # Convert transaction to bytes
    transaction_bytes = transaction.encode('utf-8')
    
    # Add transaction to log
    log.append(transaction_bytes)
    
    # Add transaction to merkle tree
    merkle_tree.add_leaf(transaction_bytes)
