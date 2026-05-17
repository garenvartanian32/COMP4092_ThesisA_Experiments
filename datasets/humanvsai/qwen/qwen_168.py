def in6_ifaceidtomac(ifaceid):
    import re
    ifaceid_regex = re.compile('^([0-9A-Fa-f]{1,4}:){0,7}[0-9A-Fa-f]{1,4}$')
    if not ifaceid_regex.match(ifaceid):
        return None
    parts = ifaceid.split(':')
    parts = [part.zfill(4) for part in parts]
    while len(parts) < 8:
        parts.append('0000')
    mac_address = ':'.join(parts[:3])
    return mac_address

def test_in6_ifaceidtomac():
    """Test the in6_ifaceidtomac function with various inputs."""