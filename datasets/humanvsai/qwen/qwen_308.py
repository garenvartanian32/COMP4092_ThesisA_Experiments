def write_key_val(stream, key, val, linesep=os.linesep):
    key_len = len(key)
    val_len = len(val)
    max_line_len = 72 - len(linesep)
    if key_len + val_len + 1 > max_line_len:
        remaining_val = val
        while remaining_val:
            max_val_len = max_line_len - key_len - 1
            if remaining_val.startswith(' '):
                max_val_len -= 1
            stream.write(key.encode('utf-8') + b' ' + remaining_val[:max_val_len].encode('utf-8') + linesep.encode('utf-8'))
            remaining_val = remaining_val[max_val_len:]
            key = ' '
    else:
        stream.write(key.encode('utf-8') + b' ' + val.encode('utf-8') + linesep.encode('utf-8'))