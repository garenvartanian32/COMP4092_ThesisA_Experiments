import socket

class SecureTransportContext:
    def __init__(self, sock):
        self.sock = sock

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        if exc_type:
            raise

# Usage
with SecureTransportContext(socket.socket()) as stc:
    # Do some I/O here
    pass