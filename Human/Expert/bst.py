class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        elif data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def PrintTree(self):
        if not self.left and not self.right: return [self.data]
        return (self.left.PrintTree() if self.left else []) + [self.data] + (self.right.PrintTree() if self.right else [])