def parse_float(float_str):
    factor = __get_factor(float_str)
    if factor != 1:
        float_str = float_str[:-1]
    try:
        return float(float_str.replace(',', '')) * factor
    except ValueError:
        return None