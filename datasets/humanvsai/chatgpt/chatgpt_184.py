import os
import zipfile

def zip_dir(path, ziph, wrapdir=False):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if wrapdir:
                ziph.write(file_path, os.path.join(os.path.basename(path), os.path.relpath(file_path, path)))
            else:
                ziph.write(file_path, os.path.relpath(file_path, path))
