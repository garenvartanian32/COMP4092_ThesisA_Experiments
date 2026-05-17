def search_and_update_node(nodes_list, ip, host):
    node = None
    updated = 0
    
    for n in nodes_list:
        if n.ip == ip and n.host == host:  # node already exists
            node = n
            break
        elif n.host == host:  # node found by host
            node = n
            if n.ip != ip:
                n.ip = ip  # update ip if not already known
                updated = 1  # mark as updated
            break
    
    return node, updated
