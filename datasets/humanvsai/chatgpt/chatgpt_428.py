import os

def get_major_minor(devpath):
    st = os.stat(devpath)
    major = os.major(st.st_rdev)
    minor = os.minor(st.st_rdev)
    return (major, minor)
