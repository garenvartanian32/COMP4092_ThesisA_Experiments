def regex_from_markers(markers):
    return re.compile('|'.join([re.escape(c) for c in markers]))