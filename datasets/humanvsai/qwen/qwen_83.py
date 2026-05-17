def pre_order(root):
    if root is None:
        return []
    return [root] + pre_order(root.left) + pre_order(root.right)

def in_order(root):
    """Perform in-order traversing. Expects tree like structure.
        Traverse in DFS fashion.
        :param root: Root tree of the parsed tree.
        :return: Sequence of nodes to traverse."""
    if root is None:
        return []
    return in_order(root.left) + [root] + in_order(root.right)

def post_order(root):
    """Perform post-order traversing. Expects tree like structure.
        Traverse in DFS fashion.
        :param root: Root tree of the parsed tree.
        :return: Sequence of nodes to traverse."""
    if root is None:
        return []
    return post_order(root.left) + post_order(root.right) + [root]

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)