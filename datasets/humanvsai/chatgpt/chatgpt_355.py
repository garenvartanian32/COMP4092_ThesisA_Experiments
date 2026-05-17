import os

def list_files_and_dirs(current, completion_type):
    if completion_type == 'file' or completion_type == 'path':
        for file_or_dir in os.listdir(current):
            if os.path.isdir(os.path.join(current, file_or_dir)):
                yield file_or_dir
            elif os.path.isfile(os.path.join(current, file_or_dir)):
                yield file_or_dir
    else:
        for file_or_dir in os.listdir(current):
            if os.path.isdir(os.path.join(current, file_or_dir)):
                yield file_or_dir
