def encode_dns_name(dns_names: Union[str, List[str]]) -> str:
    """
    Encode the given DNS names in DNS format (without compression)
    :param dns_names: A string or a list of strings representing DNS names to be encoded
    :return: The encoded DNS name
    """
    if isinstance(dns_names, str):
        dns_names = [dns_names]

    encoded_dns_name = []
    for dns_name in dns_names:
        if dns_name[-1] != '.':
            dns_name += '.'
        labels = dns_name.split('.')
        for label in labels:
            encoded_dns_label = label.encode('utf-8')
            length = len(encoded_dns_label)
            length_byte = bytes([length])
            encoded_dns_name.append(length_byte + encoded_dns_label)
    return b''.join(encoded_dns_name).decode('utf-8')
