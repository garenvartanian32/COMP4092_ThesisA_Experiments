def random_data(line_count=1, chars_per_line=80):
    divide_lines = chars_per_line * line_count
    return '\n'.join(random_line_data(chars_per_line) for x in range(int(divide_lines / chars_per_line)))