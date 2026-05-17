def send_data(self, screen_id, format_p, data):
        if not isinstance(screen_id, baseinteger):
            raise TypeError("screen_id can only be an instance of type baseinteger")
        if not isinstance(format_p, basestring):
            raise TypeError("format_p can only be an instance of type basestring")
        if not isinstance(data, list):
            raise TypeError("data can only be an instance of type list")
        for a in data[:10]:
            if not isinstance(a, basestring):
                raise TypeError(
                        "array can only contain objects of type basestring")
        progress = self._call("sendData",
                     in_p=[screen_id, format_p, data])
        progress = IProgress(progress)
        return progress