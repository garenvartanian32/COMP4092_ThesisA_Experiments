def combine_comments(comments):
    if isinstance(comments, str):
        return comments
    elif isinstance(comments, list):
        return ' '.join(comments)
    else:
        raise ValueError('Input must be a string or a list of strings')