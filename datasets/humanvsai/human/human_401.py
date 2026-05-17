def process_connection(connection, my_socket):
    if connection.closed:
        return False
    work = False
    readfd = []
    writefd = []
    if connection.needs_input > 0:
        readfd = [my_socket]
        work = True
    if connection.has_output > 0:
        writefd = [my_socket]
        work = True
    timeout = None
    deadline = connection.next_tick
    if deadline:
        work = True
        now = time.time()
        timeout = 0 if deadline <= now else deadline - now
    if not work:
        return False
    readable, writable, ignore = select.select(readfd,
                                               writefd,
                                               [],
                                               timeout)
    if readable:
        try:
            pyngus.read_socket_input(connection, my_socket)
        except Exception as e:
            # treat any socket error as
            LOG.error("Socket error on read: %s", str(e))
            connection.close_input()
            # make an attempt to cleanly close
            connection.close()
    connection.process(time.time())
    if writable:
        try:
            pyngus.write_socket_output(connection, my_socket)
        except Exception as e:
            LOG.error("Socket error on write %s", str(e))
            connection.close_output()
            # this may not help, but it won't hurt:
            connection.close()
    return True