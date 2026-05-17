async def update_status(name=None):
    if name is None:
        # Clear game presence
        await client.change_presence(activity=None)
    else:
        # Set game presence
        game = discord.Game(name=name)
        await client.change_presence(activity=game)
