import fcntl
import ctypes

def ioctl_read(fd, value, size):
    return fcntl.ioctl(fd, value, size)
