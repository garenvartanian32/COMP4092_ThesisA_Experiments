def main():
    ports = [80, 443, 22]
    timeout = 5
    host = 'example.com'
    result = tcp_ping(ports, timeout, host)
    print(result)