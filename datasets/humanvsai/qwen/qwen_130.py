def _query_pageant(msg):
    import mmap
    import os
    import struct
    import time
    pageant_shm_path = os.path.join(os.environ['TEMP'], 'pageant_shm')
    shm_fd = os.open(pageant_shm_path, os.O_RDWR)
    shm = mmap.mmap(shm_fd, mmap.PAGESIZE)
    msg_len = len(msg)
    msg_header = struct.pack('!I', msg_len)
    msg_to_send = msg_header + msg
    shm.seek(0)
    shm.write(msg_to_send)
    os.write(shm_fd, b'\x00')
    time.sleep(0.1)
    shm.seek(0)
    response_header = shm.read(4)
    response_len = struct.unpack('!I', response_header)[0]
    response = shm.read(response_len)
    shm.close()
    os.close(shm_fd)
    return response