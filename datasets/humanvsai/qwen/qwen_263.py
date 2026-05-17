def add_members(self, members):
    if not isinstance(members, str):
        raise ValueError('members must be a string')
    self.members.append(members)

def remove_members(self, members):
    """Remove a member from the members list

        :param members: member name
        :type members: str
        :return: None"""
    if not isinstance(members, str):
        raise ValueError('members must be a string')
    if members in self.members:
        self.members.remove(members)
    else:
        raise ValueError('Member not found in the list')

def list_members(self):
    """List all members in the members list

        :return: list of members
        :rtype: list"""
    return self.members