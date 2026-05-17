def can_view(self, user=None, access_code=None):
    if user and user.is_authenticated:
        if user == self.user:
            return True
        elif user.is_staff:
            return True
    if access_code and access_code == self.access_code:
        return True
    return False