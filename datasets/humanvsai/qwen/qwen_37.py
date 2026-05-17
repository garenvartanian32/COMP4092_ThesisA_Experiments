def locale_escape(string, errors='replace'):
    import locale
    import codecs
    encoding = locale.getpreferredencoding(False)
    return codecs.encode(string, encoding, errors)

def locale_unescape(string, errors='replace'):
    """Unmangle non-supported characters, for savages with ascii terminals."""
    import locale
    import codecs
    encoding = locale.getpreferredencoding(False)
    return codecs.decode(string, encoding, errors)