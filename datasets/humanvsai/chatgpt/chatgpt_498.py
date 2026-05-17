def is_stream_done(read_stream, pump):
    return (not pump.wait_for_output) and (read_stream.read() == b'')
