def _get_type(self, s):
    if s.startswith('"') and s.endswith('"'):
        return s[1:-1]
    elif s.startswith("'") and s.endswith("'"):
        return s[1:-1]
    elif s.isdigit():
        return int(s)
    elif s.replace('.', '', 1).isdigit():
        return float(s)
    else:
        raise ValueError(f'Cannot convert {s} to a known type')