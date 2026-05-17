def _process_node(self, node):
    if node.tag == 'jabber:component:accept':
        # handle authentication element
        pass
    elif node.tag == 'jabber:client' or node.tag == 'jabber:server':
        # treat elements equally
        self.process_stanza(node)
    else:
        # pass to `Stream._process_node`
        super()._process_node(node)