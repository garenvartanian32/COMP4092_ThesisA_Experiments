import os

def write_key_val(stream, key, val, linesep=os.linesep):
    """The MANIFEST specification limits the width of individual lines to
    72 bytes (including the terminating newlines). Any key and value
    pair that would be longer must be split up over multiple
    continuing lines
    :type key, val: str in Py3, str or unicode in Py2
    :type stream: binary"""

    # Convert key and value to bytes
    key_bytes = key.encode()
    val_bytes = val.encode()

    # Write key
    stream.write(key_bytes)
    stream.write(b': ')

    # If value is too long, split it into multiple lines
    while len(val_bytes) > 72:
        stream.write(val_bytes[:72])
        stream.write(linesep.encode())
        val_bytes = val_bytes[72:]

    # Write the remaining value
    stream.write(val_bytes)
    stream.write(linesep.encode())