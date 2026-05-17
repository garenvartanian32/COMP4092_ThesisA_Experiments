def rectangular_weir_width(head, length):
    """
    Returns the width of a rectangular weir.

    Parameters:
    head (numeric): The head over the weir crest in meters.
    length (numeric): The length of the weir crest in meters.

    Returns:
    (numeric): The width of the rectangular weir in meters.

    """
    gravity = 9.81  # The acceleration due to gravity in m/s^2
    width = ((2 / 3) * head ** (3 / 2)) / (gravity ** (1 / 2) * length)
    return width
