class Repository:
    def __init__(self):
        self.releases = []

    def delete(self, release):
        if release in self.releases:
            self.releases.remove(release)
            return True
        else:
            return False