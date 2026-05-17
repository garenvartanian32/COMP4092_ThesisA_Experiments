def change_username(self, username):
        username = username.lower()
        if self.username != username:
            if self.get_by_username(username):
                raise exceptions.AuthError("Username exists already")
            self.update(username=username)