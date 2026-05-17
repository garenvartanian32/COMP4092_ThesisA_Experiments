import os
import errno

def read_pty(size):
    try:
        data = os.read(fd, size)
        if not data:
            raise EOFError
        return data
    except OSError as e:
        if e.errno == errno.EIO: # handle errno=EIO pattern used on Linux
            return ''
        else:
            raise  # re-raise any other OSError
