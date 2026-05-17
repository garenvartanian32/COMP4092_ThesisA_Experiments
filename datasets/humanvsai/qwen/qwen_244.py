def get_md5_from_hexdigest(self, md5_hexdigest):
    import base64
    import hashlib
    md5_bytes = bytes.fromhex(md5_hexdigest)
    base64md5 = base64.b64encode(md5_bytes).decode('utf-8')
    return (md5_hexdigest, base64md5)