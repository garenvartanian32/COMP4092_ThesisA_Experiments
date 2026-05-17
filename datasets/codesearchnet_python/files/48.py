def portable_hash(x):
    """
    This function returns consistent hash code for builtin types, especially
    for None and tuple with None.

    The algorithm is similar to that one used by CPython 2.7

    >>> portable_hash(None)
    0
    >>> portable_hash((None, 1)) & 0xffffffff
    219750521
    """

    if sys.version_info >= (3, 2, 3) and 'PYTHONHASHSEED' not in os.environ:
        raise Exception("Randomness of hash of string should be disabled via PYTHONHASHSEED")

    if x is None:
        return 0
    if isinstance(x, tuple):
        h = 0x345678
        for i in x:
            h ^= portable_hash(i)
            h *= 1000003
            h &= sys.maxsize
        h ^= len(x)
        if h == -1:
            h = -2
        return int(h)
    return hash(x)