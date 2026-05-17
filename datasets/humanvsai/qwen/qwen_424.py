def uncomment_line(filename, line, comment='#'):
    """Uncomment line by removing the comment sign from the front of the line.

    If the file does not contain the line, the files content will not be
    changed (but the file will be touched in every case)."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for current_line in lines:
            if current_line.strip().startswith(comment + line.strip()):
                file.write(current_line[len(comment):])
            else:
                file.write(current_line)