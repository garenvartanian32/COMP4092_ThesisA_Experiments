import hashlib

def sort_hash(h):
    alphas = [c for c in h if c.isalpha()]
    digits = [c for c in h if c.isdigit()]
    return ''.join(alphas + digits)

def hash_ops(strings):
    combined = ''.join(strings)
    h1 = hashlib.sha256(combined.encode()).hexdigest()
    sorted_h = sort_hash(h1)
    h2 = hashlib.sha256(sorted_h.encode()).hexdigest()
    return h2