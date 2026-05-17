def extract_mac_address(iface_id):
    import re
    mac_address_pattern = r'^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$'
    compressed_mac_address_pattern = r'^([0-9A-Fa-f]{1,2}[:]){5}([0-9A-Fa-f]{1,2})$'
    
    if re.match(mac_address_pattern, iface_id):
        return iface_id
    elif re.match(compressed_mac_address_pattern, iface_id):
        expanded_iface_id = ''
        for segment in iface_id.split(':'):
            if len(segment) == 1:
                expanded_iface_id += '0' + segment + ':'
            else:
                expanded_iface_id += segment + ':'
        return expanded_iface_id[:-1]
    else:
        return None