def decode(value, strip=False):
    if value is None:
        return None
    if isinstance(value, bytes):
        value = value.decode('utf-8')
    if strip:
        value = value.strip()
    return value