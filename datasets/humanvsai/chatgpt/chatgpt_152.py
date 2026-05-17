import socket
import struct


def pipe_writer(sock: socket.socket, chunk_size: int):
    """
    Yields the write side of a pipe that will copy appropriately chunked values to a socket.
    :param sock: Socket object
    :param chunk_size: int representing the chunk size to write
    :return: None
    """
    while True:
        try:
            data = yield
            packed_size = struct.pack("!I", len(data))
            sock.sendall(packed_size)
            for i in range(0, len(data), chunk_size):
                sock.sendall(data[i:i + chunk_size])
        except (GeneratorExit, KeyboardInterrupt):
            return
        except Exception:
            pass
