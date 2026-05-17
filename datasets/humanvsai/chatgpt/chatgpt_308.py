def split_manifest_lines(key, val, stream):
    max_line_len = 72
    key_val_pair = key + ": " + val + "\n"
    if len(key_val_pair) <= max_line_len:
        stream.write(key_val_pair.encode())
    else:
        while len(key_val_pair) > max_line_len:
            split_index = key_val_pair.rfind(" ", 0, max_line_len)
            if split_index == -1:
                split_index = max_line_len - 1
            stream.write(key_val_pair[:split_index].encode())
            stream.write("\n ".encode())
            key_val_pair = " " + key_val_pair[split_index + 1:]
        stream.write(key_val_pair.encode())
