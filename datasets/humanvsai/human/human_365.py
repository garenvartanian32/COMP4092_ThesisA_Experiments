def GetValueByPath(self, path_segments):
    key = self.root_key
    for path_segment in path_segments:
      if isinstance(key, dict):
        try:
          key = key[path_segment]
        except KeyError:
          return None
      elif isinstance(key, list):
        try:
          list_index = int(path_segment, 10)
        except ValueError:
          return None
        key = key[list_index]
      else:
        return None
      if not key:
        return None
    return key