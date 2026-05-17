def locale_escape(string, errors='replace'):
    """Mangle non-supported characters, for savages with ascii terminals."""
    result = ""
    for char in string:
        if ord(char) > 127:  # non-ascii character
            if errors == 'replace':
                result += '?'
            elif errors == 'ignore':
                continue
            else:
                raise ValueError("unsupported error handling method")
        else:
            result += char
    return result