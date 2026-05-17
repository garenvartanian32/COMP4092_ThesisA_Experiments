def worker(sock, authenticated):
    """
    Called by a worker process after the fork().
    """
    signal.signal(SIGHUP, SIG_DFL)
    signal.signal(SIGCHLD, SIG_DFL)
    signal.signal(SIGTERM, SIG_DFL)
    # restore the handler for SIGINT,
    # it's useful for debugging (show the stacktrace before exit)
    signal.signal(SIGINT, signal.default_int_handler)

    # Read the socket using fdopen instead of socket.makefile() because the latter
    # seems to be very slow; note that we need to dup() the file descriptor because
    # otherwise writes also cause a seek that makes us miss data on the read side.
    infile = os.fdopen(os.dup(sock.fileno()), "rb", 65536)
    outfile = os.fdopen(os.dup(sock.fileno()), "wb", 65536)

    if not authenticated:
        client_secret = UTF8Deserializer().loads(infile)
        if os.environ["PYTHON_WORKER_FACTORY_SECRET"] == client_secret:
            write_with_length("ok".encode("utf-8"), outfile)
            outfile.flush()
        else:
            write_with_length("err".encode("utf-8"), outfile)
            outfile.flush()
            sock.close()
            return 1

    exit_code = 0
    try:
        worker_main(infile, outfile)
    except SystemExit as exc:
        exit_code = compute_real_exit_code(exc.code)
    finally:
        try:
            outfile.flush()
        except Exception:
            pass
    return exit_code