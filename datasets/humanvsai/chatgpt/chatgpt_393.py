def flatten(l):
    result = []
    for item in l:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
