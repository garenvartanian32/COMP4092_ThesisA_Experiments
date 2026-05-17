import os

def get_xattr_names(file_path):
    try:
        xattr_list = os.listxattr(file_path)
        return xattr_list
    except OSError as e:
        print(f"Error: {e}")
        return None
