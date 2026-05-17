def mergeValues(self, iterator):
        """ Combine the items by creator and combiner """
        # speedup attribute lookup
        creator, comb = self.agg.createCombiner, self.agg.mergeValue
        c, data, pdata, hfun, batch = 0, self.data, self.pdata, self._partition, self.batch
        limit = self.memory_limit

        for k, v in iterator:
            d = pdata[hfun(k)] if pdata else data
            d[k] = comb(d[k], v) if k in d else creator(v)

            c += 1
            if c >= batch:
                if get_used_memory() >= limit:
                    self._spill()
                    limit = self._next_limit()
                    batch /= 2
                    c = 0
                else:
                    batch *= 1.5

        if get_used_memory() >= limit:
            self._spill()