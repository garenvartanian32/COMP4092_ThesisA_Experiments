def validate(self, value):
    if not isinstance(value, int):
        return None
    if value < 0:
        return None
    if value > 100:
        return None
    return value