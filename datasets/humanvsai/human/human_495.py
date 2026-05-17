def create_group(self, title = None, parent = None, image = 1,
                     y = 2999, mon = 12, d = 28, h = 23, min_ = 59,
                     s = 59):
        if title is None:
            raise KPError("Need a group title to create a group.")
        elif type(title) is not str or image < 1 or(parent is not None and \
            type(parent) is not v1Group) or type(image) is not int:
            raise KPError("Wrong type or value for title or image or parent")
        id_ = 1
        for i in self.groups:
            if i.id_ >= id_:
                id_ = i.id_ + 1
        group = v1Group(id_, title, image, self)
        group.creation = datetime.now().replace(microsecond=0)
        group.last_mod = datetime.now().replace(microsecond=0)
        group.last_access = datetime.now().replace(microsecond=0)
        if group.set_expire(y, mon, d, h, min_, s) is False:
            group.set_expire()
        
        # If no parent is given, just append the new group at the end
        if parent is None:
            group.parent = self.root_group
            self.root_group.children.append(group)
            group.level = 0
            self.groups.append(group)
        # Else insert the group behind the parent
        else:
            if parent in self.groups:
                parent.children.append(group)
                group.parent = parent
                group.level = parent.level+1
                self.groups.insert(self.groups.index(parent)+1, group)
            else:
                raise KPError("Given parent doesn't exist")
        self._num_groups += 1
        return True