from datetime import datetime

def nearest(items, pivot):
    """Find nearest value in array, including datetimes

    Args
    ----
    items: iterable
        List of values from which to find nearest value to `pivot`
    pivot: int or float or datetime
        Value to find nearest of in `items`

    Returns
    -------
    nearest: int or float or datetime
        Value in items nearest to `pivot`
    """
    return min(items, key=lambda x: abs(x - pivot))