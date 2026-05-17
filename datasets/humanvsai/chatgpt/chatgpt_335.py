def list_blocked_users():
    """
    List the users you have blocked.
    :return: a list of :class:`~groupy.api.blocks.Block`'s
    :rtype: :class:`list`
    """
    import groupy
    # replace with appropriate authorization
    groupy.Group.list_blocks(auth_token="YOUR_AUTH_TOKEN_HERE")
