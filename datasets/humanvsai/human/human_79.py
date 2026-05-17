def tcp_ping(
    task: Task, ports: List[int], timeout: int = 2, host: Optional[str] = None
) -> Result:
    if isinstance(ports, int):
        ports = [ports]
    if isinstance(ports, list):
        if not all(isinstance(port, int) for port in ports):
            raise ValueError("Invalid value for 'ports'")
    else:
        raise ValueError("Invalid value for 'ports'")
    host = host or task.host.hostname
    result = {}
    for port in ports:
        s = socket.socket()
        s.settimeout(timeout)
        try:
            status = s.connect_ex((host, port))
            if status == 0:
                connection = True
            else:
                connection = False
        except (socket.gaierror, socket.timeout, socket.error):
            connection = False
        finally:
            s.close()
        result[port] = connection
    return Result(host=task.host, result=result)