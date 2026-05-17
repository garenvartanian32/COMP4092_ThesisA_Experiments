def __get_known_node(self, ip, host):
    node = self.known_nodes.get(ip)
    if node:
        if node.host != host:
            node.host = host
            return (node, 1)
        return (node, 0)
    node = self.known_nodes.get(host)
    if node:
        if ip not in node.ips:
            node.ips.append(ip)
            return (node, 1)
        return (node, 0)
    return (None, 0)