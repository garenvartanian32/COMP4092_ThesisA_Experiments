class Group:
    def __init__(self):
        self.members = []

    def add_members(self, members):
        if isinstance(members, list):
            self.members.extend(members)
        elif isinstance(members, str):
            self.members.append(members)
        else:
            raise ValueError("Invalid type for members. It should be either a string or a list of strings.")