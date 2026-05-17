def apply_heuristic(self, node_a, node_b, heuristic=None):
    """helper function to apply heuristic"""
    if heuristic is None:
        # If no heuristic is provided, use a default one
        heuristic = self.default_heuristic

    # Apply the heuristic
    result = heuristic(node_a, node_b)

    return result