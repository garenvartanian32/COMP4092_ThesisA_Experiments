import os
import subprocess

def return_input_paths(files, work_dir, cache=True, docker=False):
    input_paths = {}
    for file_name, file_path in files.iteritems():
        file_extension = os.path.splitext(file_path)[1]
        if file_extension == '.tar.gz':
            subprocess.check_call(['tar', '-zxvf', file_path])
            file_path = os.path.splitext(file_path)[0]        
        if not os.path.exists(file_path):
            if cache:
                raise ValueError('File {} is not cached'.format(file_name))
            else:
                raise ValueError('File {} not found at {}'.format(file_name, file_path))
        if docker:
            file_path = os.path.join(work_dir, file_name)
        input_paths[file_name] = file_path
    return input_paths
