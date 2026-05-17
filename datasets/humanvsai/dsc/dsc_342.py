def _get_all_cwlkeys(items, default_keys=None):
    cwlkeys = []
    for item in items:
        if 'cwlkey' in item:
            cwlkeys.append(item['cwlkey'])
    if default_keys:
        cwlkeys.extend(default_keys)
    return cwlkeys