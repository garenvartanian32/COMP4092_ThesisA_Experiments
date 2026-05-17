import bisect

def find_nearest(items, pivot):
    index = bisect.bisect_left(items, pivot)
    if index == 0:
        return items[0]
    if index == len(items):
        return items[-1]
    before = items[index - 1]
    after = items[index]
    if after - pivot < pivot - before:
        return after
    else:
        return before
