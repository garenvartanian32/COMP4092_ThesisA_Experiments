def group(seq):
    """Groups elements of a sequence into unique elements.

    Args:
        seq (iterable): The sequence to group.

    Returns:
        list: A list of unique elements from the sequence.

    Examples:
        >>> group([1, 1, 2])
        [1, 2]
        >>> group(['a', 'b', 'a', 'c'])
        ['a', 'b', 'c']
    """
    return list(set(seq))