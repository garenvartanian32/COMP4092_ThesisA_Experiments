import hashlib
import base64

def get_md5_from_hexdigest(md5_hexdigest):
    # Convert the hexadecimal digest to bytes
    md5_bytes = bytes.fromhex(md5_hexdigest)

    # Calculate the MD5 hash of the bytes
    md5_hash = hashlib.md5(md5_bytes)

    # Convert the MD5 hash to base64
    base64_md5 = base64.b64encode(md5_hash.digest())

    return (md5_hexdigest, base64_md5)