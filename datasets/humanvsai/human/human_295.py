def remove(item):
    if os.path.isdir(item):
        shutil.rmtree(item)
    else:
        # Assume it's a file. error if not.
        os.remove(item)