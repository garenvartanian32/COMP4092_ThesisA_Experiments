import calendar

def _get_day_of_month(other, day_option):
    """Find the day in `other`'s month that satisfies a BaseCFTimeOffset's
    onOffset policy, as described by the `day_option` argument.

    Parameters
    ----------
    other : cftime.datetime
    day_option : 'start', 'end'
        'start': returns 1
        'end': returns last day of the month

    Returns
    -------
    day_of_month : int
    """
    if day_option == 'start':
        return 1
    elif day_option == 'end':
        # Get the last day of the month
        return calendar.monthrange(other.year, other.month)[1]
    else:
        raise ValueError("Invalid day_option. Must be 'start' or 'end'")