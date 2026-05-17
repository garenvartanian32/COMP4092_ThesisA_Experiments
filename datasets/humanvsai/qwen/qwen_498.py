def is_done(self):
    return self._read_stream_done and (not self._write_stream_pending)

class StreamHandler:

    def __init__(self, read_stream, write_stream):
        self._read_stream = read_stream
        self._write_stream = write_stream
        self._read_stream_done = False
        self._write_stream_pending = False

    def read(self):
        """Reads data from the read stream."""
        data = self._read_stream.read()
        if data is None:
            self._read_stream_done = True
        return data

    def write(self, data):
        """Writes data to the write stream."""
        self._write_stream.write(data)
        self._write_stream_pending = True

    def flush(self):
        """Flushes the write stream."""
        self._write_stream.flush()
        self._write_stream_pending = False

    def is_done(self):
        """Returns True if the read stream is done and the write stream is not pending."""
        return self._read_stream_done and (not self._write_stream_pending)
read_stream = open('input.txt', 'r')
write_stream = open('output.txt', 'w')
handler = StreamHandler(read_stream, write_stream)