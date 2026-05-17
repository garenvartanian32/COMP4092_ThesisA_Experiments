def flatten_array(grid):
    """Takes a multi-dimensional array and returns a 1 dimensional array with the
    same contents."""
    result = []
    for element in grid:
        if isinstance(element, list):
            result.extend(flatten_array(element))
        else:
            result.append(element)
    return result