def merge_comments(comments):
    if isinstance(comments, str):
        return comments.strip()
    else:
        return ' '.join([comment.strip() for comment in comments])
