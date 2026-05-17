def are_partial_tuples_in_list(target_tuple, tuple_list):
    for partial_tuple in target_tuple:
        found_partial_tuple = False
        for full_tuple in tuple_list:
            if partial_tuple == full_tuple[:len(partial_tuple)]:
                found_partial_tuple = True
                break
        if not found_partial_tuple:
            return False
    return True
