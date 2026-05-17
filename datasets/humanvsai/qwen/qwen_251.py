def replace_by_key(pif, key, subs, new_key=None, remove=False):
    if isinstance(pif, dict):
        for (k, v) in list(pif.items()):
            if k == key:
                if new_key:
                    pif[new_key] = subs(v)
                if remove:
                    del pif[k]
                else:
                    pif[k] = subs(v)
            else:
                replace_by_key(v, key, subs, new_key, remove)
    elif isinstance(pif, list):
        for (i, v) in enumerate(pif):
            replace_by_key(v, key, subs, new_key, remove)