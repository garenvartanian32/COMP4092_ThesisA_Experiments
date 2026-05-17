def write_string_to_packet(packet: bytearray, string: str, length: int):
    encoded_string = string.encode('utf-8')
    if len(encoded_string) > length:
        encoded_string = encoded_string[:length]
    packet.extend(encoded_string)
    if len(encoded_string) < length:
        packet.extend(b'\0' * (length - len(encoded_string)))
