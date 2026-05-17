def prod(vars_list):
    """Returns the product of a list of variables.

    Args:
        vars_list: The list of variables to be multiplied.

    Returns:
        The product of the variables in the list.
    """
    result = 1
    for var in vars_list:
        result *= var
    return result