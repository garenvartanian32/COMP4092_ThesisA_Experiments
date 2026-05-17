def get(self, block=True, timeout=None):
        self._parent._check_closing()
        with self._parent._sync_not_empty:
            if not block:
                if not self._parent._qsize():
                    raise SyncQueueEmpty
            elif timeout is None:
                while not self._parent._qsize():
                    self._parent._sync_not_empty.wait()
            elif timeout < 0:
                raise ValueError("'timeout' must be a non-negative number")
            else:
                time = self._parent._loop.time
                endtime = time() + timeout
                while not self._parent._qsize():
                    remaining = endtime - time()
                    if remaining <= 0.0:
                        raise SyncQueueEmpty
                    self._parent._sync_not_empty.wait(remaining)
            item = self._parent._get()
            self._parent._sync_not_full.notify()
            self._parent._notify_async_not_full(threadsafe=True)
            return item