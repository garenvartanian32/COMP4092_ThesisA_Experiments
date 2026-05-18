def to_hex(text):
    values = []

    for char in text:
        values.append(format(ord(char), "x"))

    return " ".join(values)