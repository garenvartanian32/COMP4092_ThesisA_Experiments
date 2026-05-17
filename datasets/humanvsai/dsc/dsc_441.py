def decode(value, strip=False):
    if isinstance(value, bytes):
        value = value.decode()
    elif isinstance(value, str):
        pass
    elif value is None:
        value = ''
    else:
        raise TypeError('value must be a string, bytes, or None')

    if strip:
        value = value.strip()

    return value