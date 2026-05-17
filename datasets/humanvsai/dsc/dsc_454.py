class Invoice:
    def __init__(self, user, access_code):
        self.user = user
        self.access_code = access_code

    def can_view(self, user=None, access_code=None):
        if user is not None and user == self.user:
            return True
        if access_code is not None and access_code == self.access_code:
            return True
        return False