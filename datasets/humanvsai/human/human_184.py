def zipdir(src_path, target_path, wrapdir=''):
    zipf = zipfile.ZipFile(target_path, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(src_path):
        for file in files:
            path = os.path.join(root, file)
            # get the relative path from the src_path in order to avoid an archive
            # of absolute paths including your home directory.
            rel_path = os.path.relpath(path, src_path)
            zipf.write(path, os.path.join(wrapdir, rel_path))
    zipf.close()