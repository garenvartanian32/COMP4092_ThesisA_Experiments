import os
import xattr

def list_xattrs(path):
    """Get all of the xattr names for a file or directory.

    :param path: The path to the file or directory.
    :type path: str
    :rtype: list
    """
    # Check if the path exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"The path {path} does not exist.")

    # Get the list of xattr names
    xattr_names = list(xattr.xattr(path).keys())

    return xattr_names