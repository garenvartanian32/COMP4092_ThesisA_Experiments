def replace_key(pif, key, subs, new_key=None, remove=False):
    """
    Replace values that match a key

    Args:
        pif (dict): The dictionary to traverse
        key (str): The key to search for in the dictionary
        subs (Any): The value to replace the old value with
        new_key (Optional[str]): The new key to assign the replaced value to
        remove (Optional[bool]): Whether or not to remove the old key-value pair

    Returns:
        The updated dictionary

    """
    for k, v in pif.items():
        if isinstance(v, dict):
            replace_key(v, key, subs, new_key, remove)
        if k == key:
            if new_key:
                pif[new_key] = subs
            else:
                pif[k] = subs
            if remove:
                del pif[k]
    return pif
