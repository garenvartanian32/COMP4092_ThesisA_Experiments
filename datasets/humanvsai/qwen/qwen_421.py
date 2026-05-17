def _get_day_of_month(other, day_option):
    if day_option == 'start':
        return 1
    elif day_option == 'end':
        return _get_last_day_of_month(other)
    else:
        raise ValueError("Invalid day_option. Must be 'start' or 'end'.")

def _get_last_day_of_month(other):
    """Returns the last day of the month for a given cftime.datetime object.

    Parameters
    ----------
    other : cftime.datetime

    Returns
    -------
    last_day : int"""
    import calendar
    import cftime
    year = other.year
    month = other.month
    if isinstance(other, cftime._cftime.DatetimeGregorian):
        return calendar.monthrange(year, month)[1]
    else:
        last_day = cftime.num2date(cftime.date2num(cftime.datetime(year, month + 1, 1)) - 1, other.calendar)
        return last_day.day

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
    day_of_month : int"""
    if day_option == 'start':
        return 1
    elif day_option == 'end':
        return _get_last_day_of_month(other)
    else:
        raise ValueError("Invalid day_option. Must be 'start' or 'end'.")