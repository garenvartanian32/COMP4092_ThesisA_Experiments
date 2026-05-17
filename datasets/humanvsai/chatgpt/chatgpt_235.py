import random
import string

def create_random_lines(line_count, chars_per_line):
    lines = []
    for i in range(line_count):
        lines.append(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(chars_per_line)))
    return '\n'.join(lines)
