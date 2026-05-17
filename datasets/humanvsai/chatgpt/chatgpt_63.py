def parse_ranges(string):
    ranges = string.split(',')
    result = set()
    for r in ranges:
        if '-' in r:
            r_split = r.split('-')
            start = int(r_split[0])
            end_step = r_split[1].split('/')
            end = int(end_step[0])+1
            step = int(end_step[1]) if len(end_step) > 1 else 1
            result.update(range(start, end, step))
        else:
            result.add(int(r))
    return result
