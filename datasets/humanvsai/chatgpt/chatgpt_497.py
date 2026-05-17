def iterate_datetimes(start, stop, step, inclusive=False):
    """
    Iterates from `start` to `stop` datetimes with a timedelta step of `step`
    (supports iteration forwards or backwards in time)
    :param start: start datetime
    :param stop: end datetime
    :param step: step size as a timedelta
    :param inclusive: if True, last item returned will be as step closest to `end` (or `end` if no remainder).
    """
    while start <= stop:
        yield start
        start += step
    if inclusive and start - step != stop:
        yield stop
