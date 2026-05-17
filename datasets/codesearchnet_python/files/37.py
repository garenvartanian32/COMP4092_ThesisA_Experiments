def mergeCombiners(self, iterator, limit=None):
        """ Merge (K,V) pair by mergeCombiner """
        if limit is None:
            limit = self.memory_limit
        # speedup attribute lookup
        comb, hfun, objsize = self.agg.mergeCombiners, self._partition, self._object_size
        c, data, pdata, batch = 0, self.data, self.pdata, self.batch
        for k, v in iterator:
            d = pdata[hfun(k)] if pdata else data
            d[k] = comb(d[k], v) if k in d else v
            if not limit:
                continue

            c += objsize(v)
            if c > batch:
                if get_used_memory() > limit:
                    self._spill()
                    limit = self._next_limit()
                    batch /= 2
                    c = 0
                else:
                    batch *= 1.5

        if limit and get_used_memory() >= limit:
            self._spill()