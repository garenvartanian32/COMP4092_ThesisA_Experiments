def close(self):
    self._process.send('close')
    self._process.join()