def fix(x, digs):
    """Format x as [-]ddd.ddd with 'digs' digits after the point
    and at least one digit before.
    If digs <= 0, the point is suppressed."""

    # Format the number as a string
    s = f"{x:.{digs}f}"

    # If the number is negative, remove the negative sign
    if x < 0:
        s = s[1:]

    # If there are no digits after the point, remove the point
    if digs <= 0:
        s = s.replace(".", "")

    return s