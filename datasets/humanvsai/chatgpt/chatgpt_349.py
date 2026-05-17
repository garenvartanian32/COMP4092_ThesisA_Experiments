def bestscore(seq, fwd=''):
    if fwd:
        seq = fwd + seq
    scores = [0] * len(seq)
    for i in range(len(seq)):
        for j in range(i):
            if seq[i:].startswith(seq[j:]):
                scores[i] = max(scores[i], scores[j] + len(seq[j:i]))
    return max(scores)
