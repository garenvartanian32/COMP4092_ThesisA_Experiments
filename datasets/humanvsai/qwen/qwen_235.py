def random_data(line_count=1, chars_per_line=80):
    import random
    import string
    lines = []
    for _ in range(line_count):
        line = ''.join(random.choices(string.ascii_letters + string.digits, k=chars_per_line))
        lines.append(line)
    return '\n'.join(lines)