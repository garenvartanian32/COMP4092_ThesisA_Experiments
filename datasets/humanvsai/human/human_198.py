def _join_data_lines(lines, skip):
    lines = list(map(str.strip, lines))
    blank_lines = count_header_blanks(lines, skip)
    body = lines[skip + blank_lines + 2:]
    return '\n'.join(body)