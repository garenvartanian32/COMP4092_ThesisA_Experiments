def ignore_unicode_prefix(f):
    """
    Ignore the 'u' prefix of string in doc tests, to make it works
    in both python 2 and 3
    """
    if sys.version >= '3':
        # the representation of unicode string in Python 3 does not have prefix 'u',
        # so remove the prefix 'u' for doc tests
        literal_re = re.compile(r"(\W|^)[uU](['])", re.UNICODE)
        f.__doc__ = literal_re.sub(r'\1\2', f.__doc__)
    return f