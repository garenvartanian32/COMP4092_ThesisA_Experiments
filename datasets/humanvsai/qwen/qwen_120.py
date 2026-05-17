def change_username(self, username):
    if not isinstance(username, (str, email)):
        raise ValueError('Username must be a string or an email')
    self.username = username
    return self.username