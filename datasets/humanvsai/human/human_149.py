def _process_queue(self):
        if len(self._queue):
            args, kwargs = self._queue.popleft()
            self.publish(*args, **kwargs)