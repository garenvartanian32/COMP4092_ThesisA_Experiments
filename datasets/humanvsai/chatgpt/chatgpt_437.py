def construct_regex(markers):
    regex = '|'.join(re.escape(marker) for marker in markers)
    return regex