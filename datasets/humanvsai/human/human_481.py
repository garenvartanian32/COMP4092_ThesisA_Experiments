def asDictionary(self):
        template = {"type" : self._type,
                    "mapLayerId" : self._mapLayerId}
        if not self._gdbVersion is None and\
           self._gdbVersion != "":
            template['gdbVersion'] = self._gdbVersion
        return template