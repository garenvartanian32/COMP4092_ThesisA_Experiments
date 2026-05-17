def _checkPermissions(self, user, event):
    roles = self._getRoles(user)
    allowed_roles = self._getAllowedRoles(event)
    return any((role in allowed_roles for role in roles))

def _getRoles(self, user):
    """Returns a list of roles for the given user."""
    pass

def _getAllowedRoles(self, event):
    """Returns a list of roles that are allowed to fire the event."""
    pass