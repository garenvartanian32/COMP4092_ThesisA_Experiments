def parse_float(float_str):
    if not float_str:
        return None
    if float_str[-1].lower() in ['b', 'm', 'k']:
        multiplier = {'b': 1000000000.0, 'm': 1000000.0, 'k': 1000.0}[float_str[-1].lower()]
        float_str = float_str[:-1]
    else:
        multiplier = 1
    try:
        return float(float_str) * multiplier
    except ValueError:
        return None