class _BaseSourcePaths:
    def __init__(self):
        self.excludes = []

    def add_excludes(self, excludes):
        """Add a list of excludes
        :param list excludes: list of excludes"""
        self.excludes.extend(excludes)