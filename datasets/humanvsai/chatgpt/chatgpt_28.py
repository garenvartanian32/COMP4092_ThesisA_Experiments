def get_minions_by_range(minions, start=0, end=None):
    if end is None:
        end = len(minions)
    return minions[start:end]
