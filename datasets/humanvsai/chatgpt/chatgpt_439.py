import os
import zipfile

def check_files_in_directory(archive_path, target_directory):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            for file_name in zip_ref.namelist():
                file_path = os.path.join(target_directory, file_name)
                if not os.path.exists(file_path):
                    return False
        return True
