def merge_validation_result(self, new_result):
    """
    Merges another validation result graph into itself.

    Args:
        new_result (Dict): The validation result graph to be merged.

    Returns:
        Dict: The merged validation result graph.

    """
    for k, v in new_result.items():
        if k in self:
            self[k].extend(v)
        else:
            self[k] = v
    return self
