class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right
 
    def __repr__(self):
        return f"TreeNode({self.val})"
 
class BST:
    def __init__(self):
        self.root = None
 
    # ── insert ──────────────────────────────────────────────────────────────
    def insert(self, val):
        self.root = self._insert(self.root, val)
 
    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left  = self._insert(node.left,  val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node          # duplicates are silently ignored
 
    # ── search ──────────────────────────────────────────────────────────────
    def search(self, val):
        return self._search(self.root, val)
 
    def _search(self, node, val):
        if not node:
            return False
        if val == node.val:
            return True
        return self._search(node.left  if val < node.val else node.right, val)
 
    # ── delete ──────────────────────────────────────────────────────────────
    def delete(self, val):
        self.root = self._delete(self.root, val)
 
    def _delete(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left  = self._delete(node.left,  val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Node found — handle the three cases
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Two children: replace with in-order successor (leftmost in right subtree)
            successor = node.right
            while successor.left:
                successor = successor.left
            node.val   = successor.val
            node.right = self._delete(node.right, successor.val)
        return node
 
    # ── inorder traversal (returns sorted list) ─────────────────────────────
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
 
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left,  result)
            result.append(node.val)
            self._inorder(node.right, result)
 
    def __repr__(self):
        return f"BST(inorder={self.inorder()})"