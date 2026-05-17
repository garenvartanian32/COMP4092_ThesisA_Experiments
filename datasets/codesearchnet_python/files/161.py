def _load_from_socket(port, auth_secret):
    """
    Load data from a given socket, this is a blocking method thus only return when the socket
    connection has been closed.
    """
    (sockfile, sock) = local_connect_and_auth(port, auth_secret)
    # The barrier() call may block forever, so no timeout
    sock.settimeout(None)
    # Make a barrier() function call.
    write_int(BARRIER_FUNCTION, sockfile)
    sockfile.flush()

    # Collect result.
    res = UTF8Deserializer().loads(sockfile)

    # Release resources.
    sockfile.close()
    sock.close()

    return res