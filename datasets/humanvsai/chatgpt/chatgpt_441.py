def decode_output(value, strip=False):
    if value is None:
        return ""
    elif isinstance(value, bytes):
        value = value.decode()
    else:
        value = str(value)
    if strip:
        return value.strip()
    else:
        return value
