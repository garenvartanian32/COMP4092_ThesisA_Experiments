def data_packet(type, len, data):
    """
    Creates a data packet with size 32 containing the data type, data length, and raw data.

    Arguments:
    type -- the data type (uint8_t)
    len -- the data length (uint8_t)
    data -- the raw data (uint8_t)

    Returns:
    A byte string with a size of 32 bytes containing the data type, data length, and raw data.
    """
    packet = bytearray(32)
    packet[0] = type
    packet[1] = len
    packet[2:32] = data[:30]
    return bytes(packet)
