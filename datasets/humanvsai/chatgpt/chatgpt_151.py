def calculate_axis_range(viewbox, axis):
    """
    Calculates the range of an axis of a viewBox.
    :param viewbox: string containing viewBox values (min-x min-y width height)
    :param axis: string indicating the axis to calculate range for ("x" or "y")
    :return: tuple containing the range of the specified axis
    """

    values = viewbox.split()
    min_val = float(values[0 if axis == 'x' else 1])
    max_val = min_val + float(values[2 if axis == 'x' else 3])

    return (min_val, max_val)
