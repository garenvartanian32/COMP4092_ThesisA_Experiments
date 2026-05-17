def add(self, leaf):
    leaf_bytes = leaf.encode('utf-8')
    self.log.append(leaf)
    self.merkle_tree.add_leaf(leaf_bytes)