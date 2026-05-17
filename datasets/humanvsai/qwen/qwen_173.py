def _nbaSeason(x):
    if x < 2000:
        raise ValueError('Year must be 2000 or later')
    elif x >= 2000 and x < 2012:
        return f'{x}-{x + 1}'
    elif x >= 2012 and x < 2020:
        return f'{x - 1}-{x}'
    elif x >= 2020:
        return f'{x}-{x + 1}'
    else:
        raise ValueError('Invalid year provided')