def pre_order(root, tree):
    """Perform pre-order traversing. Expects tree like structure.
        Traverse in DFS fashion.
        :param root: Root node of the tree.
        :param tree: Tree structure represented as a dictionary.
        :return: Sequence of nodes to traverse."""

    # Create an empty list to store the traversal sequence
    traversal_sequence = []

    # Define a helper function to perform the traversal
    def pre_order_helper(node):
        # Add the current node to the traversal sequence
        traversal_sequence.append(node)

        # Traverse the children of the current node
        for child in tree[node]:
            pre_order_helper(child)

    # Start the traversal from the root node
    pre_order_helper(root)

    # Return the traversal sequence
    return traversal_sequence