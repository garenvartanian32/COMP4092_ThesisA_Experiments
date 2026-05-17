def _get_all_cwlkeys(items, default_keys=None):
    if default_keys is None:
        default_keys = []
    all_keys = set()
    for item in items:
        if item is not None:
            all_keys.update(item.keys())
    all_keys.update(default_keys)
    return all_keys

def _get_cwlkeys(item, all_keys):
    """Retrieve cwlkeys from a single item, filling in defaults where necessary."""
    if item is None:
        return {key: None for key in all_keys}
    return {key: item.get(key, None) for key in all_keys}

def _get_cwlkeys_list(items, all_keys):
    """Retrieve cwlkeys from a list of items, filling in defaults where necessary."""
    return [_get_cwlkeys(item, all_keys) for item in items]

def _get_cwlkeys_dict(items, all_keys):
    """Retrieve cwlkeys from a dictionary of items, filling in defaults where necessary."""
    return {key: _get_cwlkeys(value, all_keys) for (key, value) in items.items()}

def _get_cwlkeys_nested(items, all_keys):
    """Retrieve cwlkeys from nested structures, filling in defaults where necessary."""
    if isinstance(items, dict):
        return _get_cwlkeys_dict(items, all_keys)
    elif isinstance(items, list):
        return _get_cwlkeys_list(items, all_keys)
    else:
        return _get_cwlkeys(items, all_keys)

def get_cwlkeys(items, default_keys=None):
    """Main function to retrieve cwlkeys from various structures, handling defaults."""
    all_keys = _get_all_cwlkeys(items, default_keys)
    return _get_cwlkeys_nested(items, all_keys)