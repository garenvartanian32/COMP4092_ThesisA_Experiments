from urllib.parse import quote_plus

def urlencode(query, doseq=0):
    if hasattr(query, "items"):
        # Mapping objects
        mapping = query
    else:
        # Handle list of tuples
        mapping = dict(query)

    if doseq:
        for k, v in mapping.items():
            if isinstance(v, (list, tuple)):
                mapping[k] = [quote_plus(str(i)) for i in v]
            else:
                mapping[k] = quote_plus(str(v))
    else:
        for k, v in mapping.items():
            mapping[k] = quote_plus(str(v))

    return "&".join(f"{quote_plus(str(k))}={v}" for k, v in mapping.items())