def _create_body(self, name, port=None, protocol=None, nodes=None):
    body = {
        'name': name,
        'port': port,
        'protocol': protocol,
        'nodes': nodes
    }
    return body