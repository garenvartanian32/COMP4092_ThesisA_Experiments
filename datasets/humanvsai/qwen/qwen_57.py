def names2dnsrepr(x):
    if isinstance(x, str):
        if x.startswith(b'\xc0'):
            return x
        return encode_single_name(x)
    elif isinstance(x, list):
        return ''.join((encode_single_name(name) for name in x))
    else:
        raise ValueError('Input must be a string or a list of strings')

def encode_single_name(name):
    """Encodes a single DNS name into DNS format."""
    labels = name.split('.')
    encoded_labels = []
    for label in labels:
        length = len(label)
        if length > 63:
            raise ValueError('DNS label too long')
        encoded_labels.append(chr(length) + label)
    return ''.join(encoded_labels)