def write_utf(self, s):
    self.write_varint(len(s))
    self.write_bytes(s.encode('utf-8'))

def write_varint(self, value):
    """Writes a variable-length integer to the packet"""
    while True:
        byte = value & 127
        value >>= 7
        if value != 0:
            byte |= 128
        self.write_byte(byte)
        if value == 0:
            break

def write_bytes(self, b):
    """Writes bytes to the packet"""
    self.packet.extend(b)

def write_byte(self, b):
    """Writes a single byte to the packet"""
    self.packet.append(b)

def __init__(self, packet=None):
    """Initializes the packet writer with an optional initial packet"""
    if packet is None:
        packet = bytearray()
    self.packet = packet