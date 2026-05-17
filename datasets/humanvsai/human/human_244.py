def get_md5_from_hexdigest(self, md5_hexdigest):
        import binascii
        digest = binascii.unhexlify(md5_hexdigest)
        base64md5 = base64.encodestring(digest)
        if base64md5[-1] == '\n':
            base64md5 = base64md5[0:-1]
        return (md5_hexdigest, base64md5)