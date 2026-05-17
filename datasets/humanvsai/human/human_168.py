def in6_ifaceidtomac(ifaceid):
    try:
        # Set ifaceid to a binary form
        ifaceid = inet_pton(socket.AF_INET6, "::" + ifaceid)[8:16]
    except Exception:
        return None
    if ifaceid[3:5] != b'\xff\xfe':  # Check for burned-in MAC address
        return None
    # Unpacking and converting first byte of faceid to MAC address equivalent
    first = struct.unpack("B", ifaceid[:1])[0]
    ulbit = 2 * [1, '-', 0][first & 0x02]
    first = struct.pack("B", ((first & 0xFD) | ulbit))
    # Split into two vars to remove the \xff\xfe bytes
    oui = first + ifaceid[1:3]
    end = ifaceid[5:]
    # Convert and reconstruct into a MAC Address
    mac_bytes = ["%.02x" % orb(x) for x in list(oui + end)]
    return ":".join(mac_bytes)