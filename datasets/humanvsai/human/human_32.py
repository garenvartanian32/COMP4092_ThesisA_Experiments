def fullName(self):
        # join with '_' if both are set (cannot put '.', because it is used as
        # **kwargs)
        if self.parentName and self.name:
            return self.parentName + '_' + self.name
        # otherwise just use the one that is set
        # (this allows empty name for "anonymous nests")
        return self.name or self.parentName