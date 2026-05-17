def open(cls, sock, chunk_type, isatty, chunk_eof_type=None, buf_size=None, select_timeout=None):
    with cls.open_multi(sock,
                        (chunk_type,),
                        (isatty,),
                        chunk_eof_type,
                        buf_size,
                        select_timeout) as ctx:
      yield ctx