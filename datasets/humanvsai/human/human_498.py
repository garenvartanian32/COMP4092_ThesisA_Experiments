def is_done(self):
        return (not self.wait_for_output or self.eof) and \
                not (hasattr(self.to_stream, 'needs_write') and self.to_stream.needs_write())