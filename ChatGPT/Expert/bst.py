class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    def contains(self, value):
        return self._contains(self.root, value)

    def _contains(self, current, value):
        if current is None:
            return False

        if value == current.value:
            return True

        if value < current.value:
            return self._contains(current.left, value)

        return self._contains(current.right, value)

    def inorder(self):
        values = []
        self._inorder(self.root, values)
        return values

    def _inorder(self, current, values):
        if current is None:
            return

        self._inorder(current.left, values)
        values.append(current.value)
        self._inorder(current.right, values)
