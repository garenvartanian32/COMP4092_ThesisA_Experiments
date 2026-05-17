def scratch_to_python(s: str):
    if s.startswith('"') and s.endswith('"'):
        return s[1:-1]
    elif '.' in s:
        return float(s)
    else:
        return int(s)
