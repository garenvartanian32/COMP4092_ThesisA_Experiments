class Node:
    def __init__(self, ip, host):
        self.ip = ip
        self.host = host
        self.known_nodes = []

    def __get_known_node(self, ip, host):
        # Look for known nodes by IP and HOST
        for node in self.known_nodes:
            if node.ip == ip and node.host == host:
                # If found by HOST, add the IP if not already known
                if ip not in self.known_nodes:
                    self.known_nodes.append(ip)
                return node, 1  # return node and 1=updated
        return None, 0  # return None and 0=not updated