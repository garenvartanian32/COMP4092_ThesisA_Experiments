import shutil

def copy(self, target, timeout=500):
    """Copy or download this file to a new local file"""
    try:
        shutil.copy(self.file_path, target)
        print(f"File copied successfully to {target}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")