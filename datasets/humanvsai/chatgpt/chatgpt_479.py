def parse_string_to_float(s):
    suffix = s[-1]
    if suffix.isalpha():
        num = float(s[:-1])
        if suffix == 'b':
            num *= 1000000000
        elif suffix == 'm':
            num *= 1000000
        elif suffix == 'k':
            num *= 1000
        return num
    else:
        return float(s)
