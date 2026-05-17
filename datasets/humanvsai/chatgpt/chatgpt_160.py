class Node:
    def __init__(self, value):
        self.value = value

    def require_scalar(self, *args):
        if len(args) > 0:
            valid_types = args
        else:
            valid_types = (int, float, str)

        if not isinstance(self.value, valid_types):
            raise Exception(f"Invalid node type. Expected one of {valid_types}.")

# Example usage:
node = Node(5)
node.require_scalar(int, str)  # raises an exception
node.require_scalar(str, float)  # passes validation
