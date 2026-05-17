def find_all(self, collection):
    """Search a collection for all available items.

    Args:
        collection: The db collection. See main class documentation.
    Returns:
        List of all items in the collection.
    """
    return list(collection)