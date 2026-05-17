def bestscore(self,seq, fwd=''):
        matches, endpoints, scores = self._scan(seq,threshold=-100000,forw_only=fwd)
        if scores: return max(scores)
        else:      return -1000