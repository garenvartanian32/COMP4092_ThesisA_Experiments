class MyClass:
    def __init__(self, plist):
        self.plist = plist

    def GetValueByPath(self, path_segments):
        """Retrieves a plist value by path.

        Args:
          path_segments (list[str]): path segment strings relative to the root
              of the plist.

        Returns:
          object: The value of the key specified by the path or None."""

        current = self.plist
        for segment in path_segments:
            if segment in current:
                current = current[segment]
            else:
                return None
        return current