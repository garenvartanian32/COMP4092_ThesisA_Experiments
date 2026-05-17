def set_status(self, name=None):
    """Updates the bot's status

    This is used to get the game that the bot is "playing" or to clear it.
    If you want to set a game, pass a name; if you want to clear it, either
    call this method without the optional ``name`` parameter or explicitly
    pass ``None``.

    Args:
        name: the game's name, or None
    """
    if name is None:
        # Clear the status
        self.status = None
    else:
        # Set the status
        self.status = name