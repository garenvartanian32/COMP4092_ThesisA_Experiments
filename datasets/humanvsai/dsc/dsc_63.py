def _parse(self, pattern):
    """Parse string of comma-separated x-y/step -like ranges"""
    ranges = pattern.split(',')
    result = []
    for r in ranges:
        parts = r.split('/')
        if len(parts) == 1:
            # x-y range
            xy = parts[0].split('-')
            if len(xy) == 2:
                result.append((int(xy[0]), int(xy[1])))
        elif len(parts) == 2:
            # x-y/step range
            xy = parts[0].split('-')
            if len(xy) == 2:
                result.append((int(xy[0]), int(xy[1]), int(parts[1])))
    return result