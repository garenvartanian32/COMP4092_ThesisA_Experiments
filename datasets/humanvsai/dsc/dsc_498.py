class Stream:
    def __init__(self):
        self.read_stream_done = False
        self.write_stream_has_pending_bytes = False

    def is_done(self):
        """Returns True if the read stream is done (either it's returned EOF or
            the pump doesn't have wait_for_output set), and the write
            side does not have pending bytes to send."""
        return self.read_stream_done and not self.write_stream_has_pending_bytes