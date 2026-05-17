def slugify(value, separator='-', max_length=0, word_boundary=False,
            entities=True, decimal=True, hexadecimal=True):
    value = normalize('NFKD', to_string(value, 'utf-8', 'ignore'))
    if unidecode:
        value = unidecode(value)
    # character entity reference
    if entities:
        value = CHAR_ENTITY_REXP.sub(
            lambda m: chr(name2codepoint[m.group(1)]), value)
    # decimal character reference
    if decimal:
        try:
            value = DECIMAL_REXP.sub(lambda m: chr(int(m.group(1))), value)
        except Exception:
            pass
    # hexadecimal character reference
    if hexadecimal:
        try:
            value = HEX_REXP.sub(lambda m: chr(int(m.group(1), 16)), value)
        except Exception:
            pass
    value = value.lower()
    value = REPLACE1_REXP.sub('', value)
    value = REPLACE2_REXP.sub('-', value)
    # remove redundant -
    value = REMOVE_REXP.sub('-', value).strip('-')
    # smart truncate if requested
    if max_length > 0:
        value = smart_truncate(value, max_length, word_boundary, '-')
    if separator != '-':
        value = value.replace('-', separator)
    return value