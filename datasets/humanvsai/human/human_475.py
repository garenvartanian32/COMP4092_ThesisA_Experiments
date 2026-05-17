def get_var(self, name, recurse=True):
        self._dlog("getting var '{}'".format(name))
        return self._search("vars", name, recurse)