def parse(v):
    elements = v.split(',')
    result = []
    for element in elements:
        parts = element.split(':')
        if len(parts) == 1:
            result.append((int(parts[0]), int(parts[0]), 1))
        elif len(parts) == 2:
            result.append((int(parts[0]), int(parts[1]), 1))
        elif len(parts) == 3:
            result.append((int(parts[0]), int(parts[1]), int(parts[2])))
        else:
            raise ValueError('Invalid slice string')
    return result