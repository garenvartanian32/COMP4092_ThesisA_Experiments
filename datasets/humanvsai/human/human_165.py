def add(self, leaf):
        # Serializing here to avoid serialisation in `_addToStore` and
        # `_addToTree`
        serz_leaf = self.serialize_for_txn_log(leaf)
        self._addToStore(serz_leaf, serialized=True)
        serz_leaf_for_tree = self.serialize_for_tree(leaf)
        merkle_info = self._addToTree(serz_leaf_for_tree, serialized=True)
        return merkle_info