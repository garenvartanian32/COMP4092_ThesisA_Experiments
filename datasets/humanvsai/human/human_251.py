def replace_by_key(pif, key, subs, new_key=None, remove=False):
    if not new_key:
        new_key = key
        remove = False
    orig = pif.as_dictionary()
    new  = _recurse_replace(orig, to_camel_case(key), to_camel_case(new_key), subs, remove)
    return pypif.pif.loads(json.dumps(new))