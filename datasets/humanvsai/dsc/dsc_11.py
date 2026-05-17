def get_batch(sequence, size, start=0, endpoint=None, complete=False):
    if endpoint is None:
        endpoint = len(sequence)

    if complete:
        return sequence[start:endpoint]
    else:
        return sequence[start:start+size]