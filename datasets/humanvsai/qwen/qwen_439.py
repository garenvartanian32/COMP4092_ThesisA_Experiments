def check_files(self, to_path=None):
    if to_path is None:
        to_path = self.to_path
    for file in self.files:
        if not file.startswith(to_path):
            return False
    return True