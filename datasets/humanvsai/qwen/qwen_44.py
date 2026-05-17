def add_excludes(self, excludes):
    if not isinstance(excludes, list):
        raise TypeError('excludes must be a list')
    self.excludes.extend(excludes)