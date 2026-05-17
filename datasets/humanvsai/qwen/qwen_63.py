def _parse(self, pattern):
    ranges = pattern.split(',')
    parsed_ranges = []
    for range_str in ranges:
        range_str = range_str.strip()
        if '-' in range_str:
            (start, end_step) = range_str.split('-')
            start = int(start)
            if '/' in end_step:
                (end, step) = end_step.split('/')
                end = int(end)
                step = int(step)
            else:
                end = int(end_step)
                step = 1
        else:
            start = int(range_str)
            end = start
            step = 1
        parsed_ranges.append((start, end, step))
    return parsed_ranges