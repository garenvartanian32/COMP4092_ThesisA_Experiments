def _spill(self):
        """ dump the values into disk """
        global MemoryBytesSpilled, DiskBytesSpilled
        if self._file is None:
            self._open_file()

        used_memory = get_used_memory()
        pos = self._file.tell()
        self._ser.dump_stream(self.values, self._file)
        self.values = []
        gc.collect()
        DiskBytesSpilled += self._file.tell() - pos
        MemoryBytesSpilled += max(used_memory - get_used_memory(), 0) << 20