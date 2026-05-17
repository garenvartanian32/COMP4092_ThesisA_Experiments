class v1Group:

    def __init__(self, title, parent, image):
        self.title = title
        self.parent = parent
        self.image = image

    def __repr__(self):
        return f'v1Group(title={self.title}, parent={self.parent}, image={self.image})'
group = v1Group('Main Group', None, 1)
sub_group = group.create_group('Sub Group', group, 2)