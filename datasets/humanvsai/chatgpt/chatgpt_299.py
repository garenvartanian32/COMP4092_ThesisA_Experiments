def set_difference(first_set, *sets):
    result_set = set(first_set)
    for s in sets:
        result_set -= set(s)
    return result_set
