def get_LAN_NICs(datacenter_id: str, lan_id: str) -> list:
    # Connect to the datacenter
    datacenter = connect_to_datacenter(datacenter_id)

    # Retrieve LAN object from datacenter
    lan = datacenter.get_lan(lan_id)

    # Retrieve the list of NICs that are part of the LAN
    nics = []
    for server in datacenter.get_all_servers():
        for nic in server.nics:
            if nic.lan == lan:
                nics.append(nic)

    return nics
