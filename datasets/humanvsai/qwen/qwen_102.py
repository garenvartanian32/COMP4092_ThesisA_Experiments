def slugify(value, separator='-', max_length=0, word_boundary=False):
    import re
    value = re.sub('[^\\w\\s-]', '', value).strip().lower()
    if word_boundary:
        value = re.sub('(?<=\\w)(?=[A-Z])', separator, value)
    value = re.sub('[-\\s]+', separator, value)
    if max_length > 0:
        value = value[:max_length]
    return value