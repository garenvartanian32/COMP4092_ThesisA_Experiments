def add_alias(namespace, alias):
    """
    Adds an alias for the given namespace.

    Args:
    namespace: The namespace to add an alias to.
    alias: The alias to add.

    Returns:
    None
    """
    namespace.__dict__[alias] = namespace
