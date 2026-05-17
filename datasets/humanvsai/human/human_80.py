def __get_known_node(self, ip, host):
        # already known by IP ?
        for ex in self.nodes:
            for exip in ex.ip:
                if (exip == '0.0.0.0'):
                    continue
                if (exip == ip):
                    return (ex, 0)
        # already known by HOST ?
        node = self.__get_known_node_by_host(host)
        if (node != None):
            # node already known
            if (ip not in node.ip):
                node.ip.append(ip)
                return (node, 1)
            return (node, 0)
        return (None, 0)