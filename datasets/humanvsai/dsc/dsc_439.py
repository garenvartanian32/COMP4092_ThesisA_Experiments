import os
import zipfile

def check_files(archive_path, target_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        for filename in archive.namelist():
            if not os.path.isfile(os.path.join(target_dir, filename)):
                print(f"File {filename} not found in target directory.")
                return False
    print("All files are in the target directory.")
    return True