def thread(self, value: str):
        if value is not None and not isinstance(value, str):
            raise TypeError("'thread' MUST be a string")
        self._thread = value