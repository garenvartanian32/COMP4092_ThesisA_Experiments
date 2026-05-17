def is_member(self, m):
    return m in self.members

def add_member(self, m):
    """Add a user to the chatroom"""
    if m not in self.members:
        self.members.append(m)
        return True
    return False

def remove_member(self, m):
    """Remove a user from the chatroom"""
    if m in self.members:
        self.members.remove(m)
        return True
    return False