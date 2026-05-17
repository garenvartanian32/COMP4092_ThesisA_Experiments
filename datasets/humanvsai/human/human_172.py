def combine_comments(comments):
    if isinstance(comments, list):
        for idx in range(len(comments)):
            if not isinstance(comments[idx], six.string_types):
                comments[idx] = six.text_type(comments[idx])
    else:
        if not isinstance(comments, six.string_types):
            comments = [six.text_type(comments)]
        else:
            comments = [comments]
    return ' '.join(comments).strip()