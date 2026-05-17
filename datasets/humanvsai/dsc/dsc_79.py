import socket

def tcp_ping(ports, timeout=2, host='localhost'):
    result = {}
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            result[port] = True
        except:
            result[port] = False
        finally:
            sock.close()
    return result