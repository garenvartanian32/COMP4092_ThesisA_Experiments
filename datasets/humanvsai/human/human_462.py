def _free_array(self, handle: int):
        with self._lock:
            if self._arrays[handle] is not None:
                self._arrays[handle] = None
                self._count -= 1