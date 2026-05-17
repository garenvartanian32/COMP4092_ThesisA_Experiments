def get_token_nodes_from_sentence(self, sentence_root_node):
    token_nodes = []
    for node in sentence_root_node.children:
        if node.type == 'token':
            token_nodes.append(node.id)
        elif node.type == 'punct':
            token_nodes.append(node.id)
        elif node.type == 'compound':
            token_nodes.extend(self.get_token_nodes_from_sentence(node))
    return token_nodes