def data32_send(self, type, len, data, force_mavlink1=False):
    if len > 32:
        raise ValueError('Data length exceeds 32 bytes')
    if len != len(data):
        raise ValueError('Data length does not match the length of the provided data')
    if force_mavlink1:
        pass
    message = bytearray()
    message.append(type)
    message.append(len)
    message.extend(data)
    padding_length = 32 - len - 2
    if padding_length > 0:
        message.extend(bytearray(padding_length))
    return message