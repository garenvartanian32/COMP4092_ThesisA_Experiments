def lookup(self, name: str, fragment: str = None):
        if name in self._contentMap:
            symbol = self._contentMap[name]
            if fragment:
                return symbol._contentMap[fragment]
            return symbol
        return self.system.lookup(name)