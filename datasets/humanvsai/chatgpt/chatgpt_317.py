def get_valid_key(size, key):
    if isinstance(key, int):
        if key < 0 or key >= size:
            raise IndexError("Index out of range")
        return key
    elif isinstance(key, slice):
        start = key.start if key.start is not None else 0
        stop = key.stop if key.stop is not None else size
        step = key.step if key.step is not None else 1
        if start < 0 or stop <= 0 or start >= size or stop > size or step == 0:
            raise IndexError("Invalid slice")
        return slice(start, stop, step)
    elif isinstance(key, tuple):
        return tuple(get_valid_key(size[i], key[i]) for i in range(len(key)))
    else:
        raise TypeError("Invalid key type")
