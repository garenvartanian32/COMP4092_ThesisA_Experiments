def constant_pool_entries(sequence):
    return [(i, type(p).__name__, p) for i, p in enumerate(sequence)]
