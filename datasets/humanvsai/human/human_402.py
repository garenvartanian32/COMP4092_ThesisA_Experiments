def IsFileRequired(self, filename):
    if filename not in self._file_mapping:
      return False
    mapping = self._file_mapping[filename]
    return mapping['required']