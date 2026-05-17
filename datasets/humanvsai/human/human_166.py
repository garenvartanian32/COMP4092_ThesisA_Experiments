def _create_body(self, name, port=None, protocol=None, nodes=None,
            virtual_ips=None, algorithm=None, halfClosed=None, accessList=None,
            connectionLogging=None, connectionThrottle=None, healthMonitor=None,
            metadata=None, timeout=None, sessionPersistence=None,
            httpsRedirect=None):
        required = (virtual_ips, port, protocol)
        if not all(required):
            raise exc.MissingLoadBalancerParameters("Load Balancer creation "
                "requires at least one virtual IP, a protocol, and a port.")
        nodes = utils.coerce_to_list(nodes)
        virtual_ips = utils.coerce_to_list(virtual_ips)
        bad_conditions = [node.condition for node in nodes
                if node.condition.upper() not in ("ENABLED", "DISABLED")]
        if bad_conditions:
            raise exc.InvalidNodeCondition("Nodes for new load balancer must be "
                    "created in either 'ENABLED' or 'DISABLED' condition; "
                    "received the following invalid conditions: %s" %
                    ", ".join(set(bad_conditions)))
        node_dicts = [nd.to_dict() for nd in nodes]
        vip_dicts = [vip.to_dict() for vip in virtual_ips]
        body = {"loadBalancer": {
                "name": name,
                "port": port,
                "protocol": protocol,
                "nodes": node_dicts,
                "virtualIps": vip_dicts,
                "algorithm": algorithm or "RANDOM",
                "halfClosed": halfClosed,
                "accessList": accessList,
                "connectionLogging": connectionLogging,
                "connectionThrottle": connectionThrottle,
                "healthMonitor": healthMonitor,
                "metadata": metadata,
                "timeout": timeout,
                "sessionPersistence": sessionPersistence,
                "httpsRedirect": httpsRedirect,
                }}
        return body