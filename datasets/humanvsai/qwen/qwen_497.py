def daterange(start, stop, step=timedelta(days=1), inclusive=False):
    if not isinstance(start, datetime):
        raise TypeError('start must be a datetime object')
    if not isinstance(stop, datetime):
        raise TypeError('stop must be a datetime object')
    if not isinstance(step, timedelta):
        raise TypeError('step must be a timedelta object')
    if step.total_seconds() == 0:
        raise ValueError('step must not be zero')
    current = start
    while current < stop and step.total_seconds() > 0 or (current > stop and step.total_seconds() < 0):
        yield current
        current += step
    if inclusive and (current == stop or (step.total_seconds() > 0 and current < stop) or (step.total_seconds() < 0 and current > stop)):
        yield current