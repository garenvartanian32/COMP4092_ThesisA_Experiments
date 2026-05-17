import socket

def test_port_connection(ports, timeout=2, host=None):
    if not host:
        host = socket.gethostname()
    result = {}
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            result[port] = sock.connect_ex((host, port)) == 0
        except socket.error:
            result[port] = False
        finally:
            sock.close()
    return {"result": result}
