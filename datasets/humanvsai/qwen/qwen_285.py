def _process_node(self, node):
    if node.tag == 'handshake':
        self.handle_handshake(node)
    elif node.tag in ('jabber:component:accept', 'jabber:client', 'jabber:server'):
        self.process_stanza(node)
    else:
        super(Stream, self)._process_node(node)