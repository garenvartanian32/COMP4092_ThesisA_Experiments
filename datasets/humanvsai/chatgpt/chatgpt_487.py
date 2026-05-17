def add_shadow_entries(shadow_store, shadow_entries):
    """
    Adds the shadow entries to the shadow store

    :param shadow_store: dict, representing the shadow store
    :param shadow_entries: list, of dicts representing the shadow entries
    :return: None
    """
    for entry in shadow_entries:
        shadow_store[entry['id']] = entry
