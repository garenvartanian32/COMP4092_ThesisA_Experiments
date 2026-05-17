def np2str(value):
    if hasattr(value, 'dtype') and \
            issubclass(value.dtype.type, (np.string_, np.object_)) and value.size == 1:
        value = np.asscalar(value)
        if not isinstance(value, str):
            # python 3 - was scalar numpy array of bytes
            # otherwise python 2 - scalar numpy array of 'str'
            value = value.decode()
        return value
    else:
        raise ValueError("Array is not a string type or is larger than 1")