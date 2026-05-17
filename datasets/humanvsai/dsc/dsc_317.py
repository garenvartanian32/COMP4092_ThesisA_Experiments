def _cleanup_new_key(self, key, size, axis):
    """Return a key of type int, slice, or tuple that is guaranteed
        to be valid for the given dimension size.

        Raises IndexError/TypeError for invalid keys."""

    # Check if key is an integer
    if isinstance(key, int):
        if key < 0 or key >= size:
            raise IndexError("Index out of range")
        return key

    # Check if key is a slice
    elif isinstance(key, slice):
        start, stop, step = key.start, key.stop, key.step
        if start is not None and (start < 0 or start >= size):
            raise IndexError("Start index out of range")
        if stop is not None and (stop < 0 or stop > size):
            raise IndexError("Stop index out of range")
        return slice(start, stop, step)

    # Check if key is a tuple
    elif isinstance(key, tuple):
        return tuple(self._cleanup_new_key(k, size, axis) for k in key)

    # If none of the above, raise TypeError
    else:
        raise TypeError("Invalid key type")