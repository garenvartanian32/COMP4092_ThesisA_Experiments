def in6_ifaceidtomac(ifaceid):
    """Extract the mac address from provided iface ID. Iface ID is provided
    in printable format ("XXXX:XXFF:FEXX:XXXX", eventually compressed). None
    is returned on error."""

    # Split the ifaceid into parts
    parts = ifaceid.split(":")

    # Check if the ifaceid is in the correct format
    if len(parts) != 4:
        return None

    # Extract the mac address
    mac = "".join(parts)

    # Check if the mac address is in the correct format
    if len(mac) != 12:
        return None

    # Return the mac address
    return ":".join([mac[i:i+2] for i in range(0, len(mac), 2)])