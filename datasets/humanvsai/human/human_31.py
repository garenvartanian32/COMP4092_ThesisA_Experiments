def combinate(values):
        prev_v = None
        for v in values:
            if prev_v:
                if not v:
                    return prev_v
            if not v.status:
                return v
        out_values = tuple([v.value for v in values])
        return Value(True, values[-1].index, out_values, None)