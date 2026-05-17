def _get_type(self, s):
    """Converts a string from Scratch to its proper type in Python. Expects a
        string with its delimiting quotes in place. Returns either a string, 
        int or float."""
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s