def intern_atom(self, name, only_if_exists = 0):
        r = request.InternAtom(display = self.display,
                               name = name,
                               only_if_exists = only_if_exists)
        return r.atom