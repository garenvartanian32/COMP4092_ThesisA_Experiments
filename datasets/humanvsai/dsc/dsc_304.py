import fcntl

def ioctl_read(fd, request, arg):
    """An ioctl with read parameters.

    fd (int)
        File descriptor.
    request (int)
        The request code.
    arg (int)
        The argument to the ioctl call.
    """
    return fcntl.ioctl(fd, request, arg)