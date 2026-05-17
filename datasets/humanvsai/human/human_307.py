def getComicData(self, comic):
        if comic not in self.data:
            if os.path.exists(self.jsonFn(comic)):
                with codecs.open(self.jsonFn(comic), 'r', self.encoding) as f:
                    self.data[comic] = json.load(f)
            else:
                self.data[comic] = {'pages':{}}
        return self.data[comic]