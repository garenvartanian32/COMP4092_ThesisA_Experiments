def get_token_nodes_from_sentence(self, sentence_root_node):
        return spanstring2tokens(self, self.node[sentence_root_node][self.ns+':span'])