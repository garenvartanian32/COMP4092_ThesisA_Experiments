def data32_send(self, type, len, data, force_mavlink1=False):
    """Data packet, size 32

    Args:
        type (uint8_t): data type
        len (uint8_t): data length
        data (uint8_t): raw data
        force_mavlink1 (bool, optional): Force MAVLink v1. Defaults to False.
    """
    # Your code here