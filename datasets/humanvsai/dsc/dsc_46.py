class MyView:
    def __init__(self):
        self.media = []

    def add_media(self, item):
        self.media.append(item)

    def get_media(self):
        return self.media