import os
import shutil

def remove(item):
    """Delete item, whether it's a file, a folder, or a folder
    full of other files and folders."""
    if os.path.isfile(item):
        os.remove(item)
    elif os.path.isdir(item):
        shutil.rmtree(item)
    else:
        print(f"{item} does not exist")