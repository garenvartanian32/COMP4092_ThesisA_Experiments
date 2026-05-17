def comment_out_line(filename: str, line_to_comment: str):
    try:
        with open(filename, 'r') as f:
            file_lines = f.readlines()

        with open(filename, 'w') as f:
            for line in file_lines:
                if line.strip() == line_to_comment:
                    f.write('#' + line)
                else:
                    f.write(line)
    except FileNotFoundError:
        open(filename, 'w').close()
