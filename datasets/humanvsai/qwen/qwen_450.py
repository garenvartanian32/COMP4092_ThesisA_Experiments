def read_checksum_digest(path, checksum_cls=hashlib.sha256):
    with open(path, 'rb') as f:
        checksum = checksum_cls()
        size = 0
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            checksum.update(chunk)
            size += len(chunk)
    return (checksum.hexdigest(), size)

def verify_checksum(path, expected_checksum, checksum_cls=hashlib.sha256):
    """Verifies the checksum of a file against an expected checksum."""
    (actual_checksum, _) = read_checksum_digest(path, checksum_cls)
    return actual_checksum == expected_checksum