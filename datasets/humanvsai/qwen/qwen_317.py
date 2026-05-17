def _cleanup_new_key(self, key, size, axis):
    if isinstance(key, int):
        if key < 0:
            key += size
        if key < 0 or key >= size:
            raise IndexError('Index out of range')
        return key
    elif isinstance(key, slice):
        (start, stop, step) = (key.start, key.stop, key.step)
        if start is None:
            start = 0
        if stop is None:
            stop = size
        if step is None:
            step = 1
        if start < 0:
            start += size
        if stop < 0:
            stop += size
        if start < 0 or stop < 0 or start >= size or (stop > size):
            raise IndexError('Slice out of range')
        return slice(start, stop, step)
    elif isinstance(key, tuple):
        if len(key) != axis:
            raise TypeError('Tuple key must have the same length as the number of axes')
        return tuple((self._cleanup_new_key(subkey, size, 1) for subkey in key))
    else:
        raise TypeError('Key must be an int, slice, or tuple')