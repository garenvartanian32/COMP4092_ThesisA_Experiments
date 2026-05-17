def comment_out_line(filename, line, comment='#'):
    """Comment line out by putting a comment sign in front of the line.

    If the file does not contain the line, the files content will not be
    changed (but the file will be touched in every case)."""

    with open(filename, 'r') as f:
        lines = f.readlines()

    for i, l in enumerate(lines):
        if line in l:
            if not l.strip().startswith(comment):
                lines[i] = comment + ' ' + l.strip() + '\n'

    with open(filename, 'w') as f:
        f.writelines(lines)