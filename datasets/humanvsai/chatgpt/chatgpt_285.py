def process_first_level_element(self, node):
    if node.tag == '{jabber:component:accept}accept':
        self.authenticated = True
    elif node.tag in ['{jabber:client}', '{jabber:server}', '{jabber:component:accept}']:
        self.process_stanza(node)
    else:
        self._process_node(node)
