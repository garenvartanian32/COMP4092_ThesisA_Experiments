import os

def _getDevMajorMinor(self, devpath):
    """Return major and minor device number for block device path devpath.
        @param devpath: Full path for block device.
        @return:        Tuple (major, minor)."""
    stat = os.stat(devpath)
    major = os.major(stat.st_rdev)
    minor = os.minor(stat.st_rdev)
    return (major, minor)