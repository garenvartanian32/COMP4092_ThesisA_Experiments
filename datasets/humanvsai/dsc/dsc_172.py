def combine_comments(comments):
    if isinstance(comments, str):
        return comments
    elif isinstance(comments, list):
        return ' '.join(comments)
    else:
        return "Invalid input"