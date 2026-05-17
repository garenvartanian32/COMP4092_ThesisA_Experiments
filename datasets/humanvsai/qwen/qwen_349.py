def bestscore(self, seq, fwd=''):
    best_score = float('-inf')
    for i in range(len(seq)):
        for j in range(i + 1, len(seq) + 1):
            subseq = seq[i:j]
            score = self.score(subseq, fwd)
            if score > best_score:
                best_score = score
    return best_score