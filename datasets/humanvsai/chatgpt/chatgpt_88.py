from calcrepo.index import count

def count_wrapper(data, start=0, end=None, step=1):
    return count(data, start=start, end=end, step=step)
