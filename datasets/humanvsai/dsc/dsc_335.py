class User:
    def __init__(self):
        self.blocked_users = []

    def block_user(self, user):
        self.blocked_users.append(user)

    def list_blocked_users(self):
        return self.blocked_users