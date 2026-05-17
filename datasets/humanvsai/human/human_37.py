def locale_escape(string, errors='replace'):
    encoding = locale.getpreferredencoding()
    string = string.encode(encoding, errors).decode('utf8')
    return string