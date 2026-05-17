def decode_url(url, charset='utf-8'):
    from urllib.parse import urlparse, unquote
    parsed_url = urlparse(url)
    decoded_url = []
    for part in parsed_url:
        if part:
            if isinstance(part, bytes):
                part = part.decode(charset)
            decoded_url.append(unquote(part, charset))
        else:
            decoded_url.append('')
    return tuple(decoded_url)
