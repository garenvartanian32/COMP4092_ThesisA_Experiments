def _join_data_lines(lines, skip):
    """Join all the data lines into a byte string"""
    # Check if skip is a valid index
    if skip >= len(lines):
        return None

    # Join the lines into a byte string
    byte_string = b''.join(lines[skip:])

    return byte_string