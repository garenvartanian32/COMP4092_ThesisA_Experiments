def tuple_partial_cmp_always(target_tuple, tuple_list, ducktype):
    """Whether partial target_tuple are always in tuple_list or not"""
    for tup in tuple_list:
        if not ducktype(tup, target_tuple):
            return False
    return True

def ducktype(t1, t2):
    """Check if t1 is a sub-tuple of t2"""
    return all(elem in t2 for elem in t1)