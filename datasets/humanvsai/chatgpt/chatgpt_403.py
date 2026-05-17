import SecureTransport

class SecureIOMgr:
    def __init__(self, sock):
        self.sock = sock
    def __enter__(self):
        SecureTransport.set_IO_callbacks(self.sock)
        return self.sock
    def __exit__(self, exc_type, exc_val, exc_tb):
        SecureTransport.remove_IO_callbacks(self.sock)
        SecureTransport.force_close_socket(self.sock)
        if exc_type is not None:
            return False
