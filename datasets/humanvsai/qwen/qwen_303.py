def decode(self, charset='utf-8', errors='replace'):
    rv = []
    for part in self._parts:
        if part.is_encoded:
            decoded_part = part.decode(charset, errors)
        else:
            decoded_part = part
        rv.append(decoded_part)
    return tuple(rv)