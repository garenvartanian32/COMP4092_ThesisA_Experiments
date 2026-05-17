def get_lan_members(self, datacenter_id, lan_id, depth=1):
    # Assuming you have a list of NICs
    nics = [
        {'id': 'nic1', 'datacenter_id': 'dc1', 'lan_id': 'lan1'},
        {'id': 'nic2', 'datacenter_id': 'dc1', 'lan_id': 'lan1'},
        {'id': 'nic3', 'datacenter_id': 'dc2', 'lan_id': 'lan2'},
        # ...
    ]

    # Filter the NICs based on the datacenter_id and lan_id
    lan_members = [nic for nic in nics if nic['datacenter_id'] == datacenter_id and nic['lan_id'] == lan_id]

    return lan_members