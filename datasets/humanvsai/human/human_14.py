def of_pyobj(self, pyobj):
        m = self.hash_algo()
        m.update(pickle.dumps(pyobj, protocol=self.pk_protocol))
        return self.digest(m)