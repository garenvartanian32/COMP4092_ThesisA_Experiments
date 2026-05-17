def streamify_frame(frame):
    """
    Serialize a frame to binary format and
    prepend the length of the serialized frame
    as a 4-byte integer in network byte order.
    """
    serialized_frame = pickle.dumps(frame)
    frame_length = struct.pack("!I", len(serialized_frame))
    return frame_length + serialized_frame
