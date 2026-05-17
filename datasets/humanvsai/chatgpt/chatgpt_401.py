import select

def handle_io_and_timers(connection, read_timeout, write_timeout):
    try:
        while True:
            r, w, e = select.select([connection], [connection], [], read_timeout)
            if not (r or w or e):
                continue
            if r:
                # handle read event
                data = connection.recv(1024)
                # do something with received data
            if w:
                # handle write event
                connection.send(b"Hello, World!")
                # do something after sending
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        connection.close()
