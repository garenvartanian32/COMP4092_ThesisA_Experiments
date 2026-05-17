import base64

def create_tuple_from_md5(md5_hexdigest):
    byte_string = md5_hexdigest.encode('utf-8')
    base64_md5 = base64.b64encode(byte_string).decode('utf-8')
    return (md5_hexdigest, base64_md5)
