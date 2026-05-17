def merge_tags(config_tags, dynamic_tags):
    """
    Given two lists of tags, merges them and returns a unique list of tags containing all elements.

    Args:
        config_tags (List[str]): List of configuration tags
        dynamic_tags (List[str]): List of dynamically applied tags.

    Returns:
        List[str]: A merged list of configuration and dynamic tags.
    """

    tags = set(config_tags + dynamic_tags)
    return list(tags)
