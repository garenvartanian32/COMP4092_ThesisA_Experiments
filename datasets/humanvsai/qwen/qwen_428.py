def _getDevMajorMinor(self, devpath):
    import os
    import stat
    st = os.stat(devpath)
    major = os.major(st.st_rdev)
    minor = os.minor(st.st_rdev)
    return (major, minor)