class Chatroom:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def is_member(self, member):
        return member in self.members