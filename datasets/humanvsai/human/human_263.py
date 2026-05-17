def add_members(self, members):
        if not isinstance(members, list):
            members = [members]
        if not getattr(self, 'members', None):
            self.members = members
        else:
            self.members.extend(members)