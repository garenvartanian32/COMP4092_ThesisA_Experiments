def find_tolerance(numbers):
    """
    Find appropriate integer tolerance for gap-filling problems.
    The function receives a list of integers and decides on the appropriate tolerance
    value to be used in order to fill any gaps between consecutive integers.
    """
    tolerance = 1
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i-1] > tolerance:
            tolerance = numbers[i] - numbers[i-1]
    return tolerance
