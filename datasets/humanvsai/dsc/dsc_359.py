def validate(self, value):
    """Applies the validation criteria.
    Returns value if it's a positive integer, otherwise returns None."""
    if isinstance(value, int) and value > 0:
        return value
    else:
        return None