import os

def read_checksum_digest(path, checksum_cls=hashlib.sha256):
    """Given a hash constructor, returns checksum digest and size of file."""
    checksum = checksum_cls()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            checksum.update(chunk)
    return checksum.hexdigest(), os.path.getsize(path)