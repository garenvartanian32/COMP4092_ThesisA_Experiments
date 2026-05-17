def set_attributes(obj, d):
    """Set attributes from dictionary of values."""
    for key, value in d.items():
        setattr(obj, key, value)