def pretty_constants(self):
        for i in range(1, len(self.consts)):
            t, v = self.pretty_const(i)
            if t:
                yield (i, t, v)