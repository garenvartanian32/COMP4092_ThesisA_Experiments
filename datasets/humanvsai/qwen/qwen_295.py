def remove(item):
    import os
    import shutil
    if os.path.isfile(item):
        os.remove(item)
    elif os.path.isdir(item):
        shutil.rmtree(item)
    else:
        print(f'Item {item} does not exist or is not a file or directory.')