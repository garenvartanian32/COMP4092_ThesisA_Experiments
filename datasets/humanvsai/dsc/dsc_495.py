def create_group(self, title = None, parent = None, image = 1):
    """
    This method creates a new group.

    A group title is needed or no group will be created.

    If a parent is given, the group will be created as a sub-group.

    title must be a string, image an unsigned int >0 and parent a v1Group.

    With y, mon, d, h, min_ and s you can set an expiration date like on
    entries.
    """
    if title is None:
        print("A group title is needed or no group will be created.")
        return

    if not isinstance(title, str):
        print("Title must be a string.")
        return

    if not isinstance(image, int) or image <= 0:
        print("Image must be an unsigned int >0.")
        return

    if parent is not None and not isinstance(parent, v1Group):
        print("Parent must be a v1Group.")
        return

    # Your code to create the group goes here