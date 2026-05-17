def write_utf(self, s):
    """Writes a UTF-8 string of a given length to the packet"""
    # Convert the string to UTF-8
    utf_string = s.encode('utf-8')

    # Write the UTF-8 string to the packet
    # This will depend on how your packet is structured
    # For example, if your packet is a list of bytes, you could do:
    self.packet.extend(utf_string)