def tuple_partial_cmp_always(target_tuple, tuple_list, ducktype):
    for t in tuple_list:
        if not all((item in t for item in target_tuple)):
            return False
    return True

def tuple_partial_cmp_any(target_tuple, tuple_list, ducktype):
    """Whether partial target_tuple are in any of the tuples in tuple_list"""
    for t in tuple_list:
        if all((item in t for item in target_tuple)):
            return True
    return False

def tuple_partial_cmp(target_tuple, tuple_list, ducktype, cmp_type='always'):
    """Compare partial target_tuple with tuple_list based on cmp_type"""
    if cmp_type == 'always':
        return tuple_partial_cmp_always(target_tuple, tuple_list, ducktype)
    elif cmp_type == 'any':
        return tuple_partial_cmp_any(target_tuple, tuple_list, ducktype)
    else:
        raise ValueError("cmp_type must be 'always' or 'any'")
target_tuple = (1, 2)
tuple_list = [(1, 2, 3), (4, 5, 6), (1, 2, 7)]