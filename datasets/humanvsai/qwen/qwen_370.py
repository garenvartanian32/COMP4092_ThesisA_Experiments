def _send_streamify(self, frame):
    if not isinstance(frame, bytes):
        raise TypeError('Frame must be of type bytes')
    self._stream.write(frame)

def _receive_streamify(self, size):
    """Helper method to receive a streamified frame."""
    if not isinstance(size, int):
        raise TypeError('Size must be of type int')
    return self._stream.read(size)

def _send_message(self, message):
    """Send a message over the stream."""
    if not isinstance(message, str):
        raise TypeError('Message must be of type str')
    frame = message.encode('utf-8')
    self._send_streamify(frame)

def _receive_message(self, size):
    """Receive a message from the stream."""
    if not isinstance(size, int):
        raise TypeError('Size must be of type int')
    frame = self._receive_streamify(size)
    return frame.decode('utf-8')

def _send_json(self, data):
    """Send JSON data over the stream."""
    if not isinstance(data, dict):
        raise TypeError('Data must be of type dict')
    json_str = json.dumps(data)
    self._send_message(json_str)

def _receive_json(self, size):
    """Receive JSON data from the stream."""
    if not isinstance(size, int):
        raise TypeError('Size must be of type int')
    json_str = self._receive_message(size)
    return json.dumps(json_str)

def _receive_json(self, size):
    """Receive JSON data from the stream."""
    if not isinstance(size, int):
        raise TypeError('Size must be of type int')
    json_str = self._receive_message(size)
    return json.loads(json_str)