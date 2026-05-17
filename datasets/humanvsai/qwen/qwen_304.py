def IOR(type, nr, size):
    import fcntl
    import ctypes
    request = type << 8 | nr & 255 | ctypes.sizeof(size) << 16
    result = fcntl.ioctl(fd, request, size)
    return result