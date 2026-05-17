def include_file(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()
    program = file_content.split('\n')
    _ENDFILE_ = program.pop()
    return program, _ENDFILE_
