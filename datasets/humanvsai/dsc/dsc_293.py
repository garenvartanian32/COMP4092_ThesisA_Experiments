def open_file(self, name, mode='r', *args, **kwargs):
    """Find a resource and return a file object, or raise IOError."""
    try:
        return open(name, mode, *args, **kwargs)
    except IOError as e:
        raise e