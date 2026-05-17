def get(self, block=True, timeout=None):
    with self.mutex:
        if not block:
            if not self.queue:
                raise Empty
            return self._get()
        elif timeout is None:
            while not self.queue:
                self.not_empty.wait()
            item = self._get()
            self.not_full.notify()
            return item
        elif timeout < 0:
            raise ValueError("'timeout' must be a non-negative number")
        else:
            endtime = time.time() + timeout
            while not self.queue:
                remaining = endtime - time.time()
                if remaining <= 0.0:
                    raise Empty
                self.not_empty.wait(remaining)
            item = self._get()
            self.not_full.notify()
            return item