import random
import string

def random_data(line_count=1, chars_per_line=80):
    result = []
    for _ in range(line_count):
        line = ''.join(random.choice(string.ascii_letters) for _ in range(chars_per_line))
        result.append(line)
    return '\n'.join(result)