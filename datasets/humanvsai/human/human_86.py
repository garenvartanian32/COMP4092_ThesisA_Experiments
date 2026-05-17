def merge(self, another):
        if isinstance(another, Result):
            another = another.errors
        self.errors = self.merge_errors(self.errors, another)