def urlencode(query, doseq=0):
    if hasattr(query, 'items'):
        query = query.items()
    else:
        query = list(query)
    l = []
    for (k, v) in query:
        if doseq and isinstance(v, (tuple, list)):
            for value in v:
                l.append('%s=%s' % (quote_plus(k, safe=''), quote_plus(value, safe='')))
        else:
            l.append('%s=%s' % (quote_plus(k, safe=''), quote_plus(v, safe='')))
    return '&'.join(l)

def quote_plus(s, safe=''):
    """Like quote(), but also replaces spaces with '+'. This is used for encoding query strings."""
    return quote(s, safe=safe + ' ').replace(' ', '+')

def quote(s, safe=''):
    """Percent-encode a string, except for characters in safe."""
    safe = set(safe)
    res = []
    for c in s:
        if c in safe:
            res.append(c)
        else:
            res.append('%%%02X' % ord(c))
    return ''.join(res)
test_query = {'key1': 'value1', 'key2': ['value2', 'value3']}