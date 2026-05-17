def items(self):
        """ Return all merged items as iterator """
        if not self.pdata and not self.spills:
            return iter(self.data.items())
        return self._external_items()