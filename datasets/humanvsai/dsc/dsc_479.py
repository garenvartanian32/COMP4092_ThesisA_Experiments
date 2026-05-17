def parse_float(float_str):
    """Parse a string of the form 305.48b into a Python float.
       The terminal letter, if present, indicates e.g. billions."""
    if float_str[-1].isalpha():
        # Get the multiplier based on the last character
        multiplier = {
            'k': 1000,
            'm': 1000000,
            'b': 1000000000,
            't': 10000000000000
        }.get(float_str[-1].lower(), 1)

        # Remove the last character and parse the float
        float_str = float_str[:-1]
        return float(float_str) * multiplier
    else:
        return float(float_str)

# Test the function
print(parse_float('305.48b'))  # Output: 305480000000.0
print(parse_float('305.48m'))  # Output: 30548000.0
print(parse_float('305.48'))   # Output: 305.48