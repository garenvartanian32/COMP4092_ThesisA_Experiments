def decode(value, strip=False):
    if value is None:
        return None
    if isinstance(value, bytes) and not isinstance(value, unicode):
        value = value.decode("utf-8")
    if strip:
        return unicode(value).strip()
    return unicode(value)