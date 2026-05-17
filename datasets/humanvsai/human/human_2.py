def parse(v):
        parts = v.split(',')
        slices = []
        for part in parts:
            p = part.split(':')
            if len(p) == 1:
                slices.append(int(p[0]))
            elif len(p) == 2:
                slices.append(tuple(p))
            else:
                raise ValueError("Too many ':': {}".format(part))
        return slices