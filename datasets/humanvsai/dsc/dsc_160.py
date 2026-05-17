def require_scalar(self, *args):
    """Require the node to be a scalar.

    If additional arguments are passed, these are taken as a list
    of valid types; if the node matches one of these, then it is
    accepted.

    Example:
        # Match either an int or a string
        node.require_scalar(int, str)

    Arguments:
        args: One or more types to match one of.
    """
    if not args:
        # If no arguments are passed, we require the node to be a scalar
        if not isinstance(self, (int, float, complex)):
            raise ValueError("Node is not a scalar")
    else:
        # If arguments are passed, we require the node to be one of these types
        if not isinstance(self, args):
            raise ValueError(f"Node is not one of the types: {args}")