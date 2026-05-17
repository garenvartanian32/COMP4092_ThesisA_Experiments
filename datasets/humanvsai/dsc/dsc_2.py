def parse(v):
    slices = v.split(',')
    result = []
    for s in slices:
        if ':' in s:
            start, end = map(int, s.split(':'))
            result.append((start, end))
        else:
            result.append((int(s), int(s)+1))
    return result