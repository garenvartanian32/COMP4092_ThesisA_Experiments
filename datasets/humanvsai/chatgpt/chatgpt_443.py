import urllib.parse

def urlencode(query, doseq=False, safe=''):
    if hasattr(query, 'items'):
        query = list(query.items())
    else:
        query = list(query)
    encoded_query = []
    for k, v in query:
        if isinstance(k, str):
            k = k.encode('utf-8')
        if isinstance(v, str):
            v = v.encode('utf-8')
        elif isinstance(v, (tuple, list)):
            if doseq:
                for vv in v:
                    if isinstance(vv, str):
                        vv = vv.encode('utf-8')
                    encoded_query.append((k, vv))
                continue
            else:
                v = urllib.parse.urlencode(v, doseq=False, safe=safe)
        else:
            v = str(v).encode('utf-8')
        k = urllib.parse.quote(k, safe=safe)
        v = urllib.parse.quote(v, safe=safe)
        encoded_query.append((k, v))
    return '&'.join([k + '=' + v for k, v in encoded_query])