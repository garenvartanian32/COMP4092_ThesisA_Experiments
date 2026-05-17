class User:
    def __init__(self, roles):
        self.roles = roles

class Role:
    def __init__(self, can_fire_event):
        self.can_fire_event = can_fire_event

    def canFireEvent(self):
        return self.can_fire_event

def _checkPermissions(self, user, event):
    """Checks if the user has in any role that allows to fire the event."""
    for role in user.roles:
        if role.canFireEvent():
            return True
    return False