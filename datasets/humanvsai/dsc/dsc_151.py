def viewBoxAxisRange(viewBox, axisNumber):
    """Calculates the range of an axis of a viewBox."""
    axis_values = [point[axisNumber] for point in viewBox]
    return min(axis_values), max(axis_values)