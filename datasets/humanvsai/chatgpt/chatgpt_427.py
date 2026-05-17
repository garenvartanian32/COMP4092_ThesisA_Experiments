def compare_and_pop_stack_top_two_strings(stack):
    """
    Compares & pops top 2 strings out of the stack.
    Temporal values are freed from memory. (a$ != b$)

    Args:
        stack (list): A list representing the stack of strings.

    Returns:
        None
    """
    if len(stack) >= 2:
        a = stack.pop()
        b = stack.pop()
        if a != b:
            return
    else:
        return
