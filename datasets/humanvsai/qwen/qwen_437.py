def regex_from_markers(markers):
    escaped_markers = [re.escape(marker) for marker in markers]
    regex_pattern = '|'.join(escaped_markers)
    return regex_pattern
markers = ['$', '(', ')', '[', ']', '{', '}']
regex = regex_from_markers(markers)