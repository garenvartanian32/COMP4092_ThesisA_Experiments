def copy(self, target, timeout=500):
    if not isinstance(target, str):
        raise ValueError('Target must be a string representing a file path')
    if not self.exists():
        raise FileNotFoundError('Source file does not exist')
    if not self.is_file():
        raise ValueError('Source is not a file')
    if not os.path.isdir(os.path.dirname(target)):
        raise ValueError('Target directory does not exist')
    if timeout <= 0:
        raise ValueError('Timeout must be a positive integer')
    try:
        shutil.copy2(self.path, target)
    except Exception as e:
        raise RuntimeError(f'Failed to copy file: {e}')
    if not os.path.exists(target):
        raise RuntimeError('File was not copied successfully')
    return target