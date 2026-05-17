import hashlib

class MerkleTree:
    def __init__(self):
        self.log = []
        self.tree = []

    def add(self, leaf):
        # Serialize the leaf and convert it to bytes
        serialized_leaf = str(leaf).encode('utf-8')

        # Add the serialized leaf to the log
        self.log.append(serialized_leaf)

        # Calculate the hash of the serialized leaf
        leaf_hash = hashlib.sha256(serialized_leaf).hexdigest()

        # Add the hash to the Merkle tree
        self.tree.append(leaf_hash)

        return leaf_hash