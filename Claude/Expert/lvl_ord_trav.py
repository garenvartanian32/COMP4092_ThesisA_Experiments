class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right
 
def __repr__(self):
        return f"TreeNode({self.val})"
 def level_order(root):
    if not root:
        return []
 
    result = []
    queue  = deque([root])
 
    while queue:
        level_vals = []
        for _ in range(len(queue)):       # process one level at a time
            node = queue.popleft()
            level_vals.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_vals)
 
    return result
 