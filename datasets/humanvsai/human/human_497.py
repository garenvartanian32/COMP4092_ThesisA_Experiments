def daterange(start, stop, step=timedelta(days=1), inclusive=False):
    # inclusive=False to behave like range by default
    total_step_secs = step.total_seconds()
    assert total_step_secs != 0
    if total_step_secs > 0:
        while start < stop:
            yield start
            start = start + step
    else:
        while stop < start:
            yield start
            start = start + step
    if inclusive and start == stop:
        yield start