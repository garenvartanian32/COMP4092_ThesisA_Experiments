def nearest(items, pivot):
    nearest = min(items, key=lambda x: abs(x - pivot))
    return nearest