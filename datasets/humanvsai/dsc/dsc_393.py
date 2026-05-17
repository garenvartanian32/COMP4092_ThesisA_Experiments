def flatten(l):
    """Flattens a hierarchy of nested lists into a single list containing all elements in order

    :param l: list of arbitrary types and lists
    :returns: list of arbitrary types"""
    flat_list = []
    for sublist in l:
        if isinstance(sublist, list):
            for item in flatten(sublist):
                flat_list.append(item)
        else:
            flat_list.append(sublist)
    return flat_list