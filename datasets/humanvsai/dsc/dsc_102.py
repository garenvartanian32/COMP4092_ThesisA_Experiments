import re

def slugify(value, separator='-', max_length=0, word_boundary=False):
    """Normalizes string, removes non-alpha characters,
    and converts spaces to ``separator`` character"""

    # Remove non-word characters (alphanumeric and underscores)
    value = re.sub('[^\w\s]','', value)

    # Replace spaces with separator
    value = re.sub('[%s\s]+' % separator, separator, value)

    # Remove leading/trailing separator
    value = re.sub('^%s|%s$' % (separator, separator), '', value)

    # Truncate to max_length
    if max_length:
        value = value[:max_length]

    return value.lower()