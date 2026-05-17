import os
import zipfile

def zipdir(src_path, target_path, wrapdir=''):
    """
    Zips the directory and its contents
    :param src_path: the path to the directory to be zipped
    :param target_path: the path to the output zip file
    :param wrapdir: wrap all contents in an additional dir
    :return:
    """
    zipf = zipfile.ZipFile(target_path, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(src_path):
        for file in files:
            if wrapdir:
                zipf.write(os.path.join(root, file), 
                          os.path.join(wrapdir, os.path.relpath(os.path.join(root, file), 
                          os.path.join(src_path, '..'))))
            else:
                zipf.write(os.path.join(root, file), 
                          os.path.relpath(os.path.join(root, file), src_path))
    zipf.close()