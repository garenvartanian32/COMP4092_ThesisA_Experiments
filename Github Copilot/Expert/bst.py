class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def PrintTree(self):
        result = []
        if self.left:
            result += self.left.PrintTree()
        result.append(self.data)
        if self.right:
            result += self.right.PrintTree()
        return result