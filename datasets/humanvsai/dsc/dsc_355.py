import os
import glob

def auto_complete_paths(current, completion_type):
    if completion_type == 'file':
        for file in glob.glob(current + '*'):
            if os.path.isfile(file):
                yield file
    elif completion_type == 'path':
        for path in glob.glob(current + '*'):
            yield path
    elif completion_type == 'dir':
        for dir in glob.glob(current + '*/'):
            yield dir
    else:
        raise ValueError('Invalid completion type')

# Example usage:
for file in auto_complete_paths('test', 'file'):
    print(file)