def get_batch(sequence, size, start=0, endpoint=None, complete=False):
    if endpoint is None:
        endpoint = len(sequence)
    if complete and endpoint - start < size:
        return sequence[start:endpoint]
    return sequence[start:start + size]