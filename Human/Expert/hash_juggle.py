from hashlib import sha256

def hash_ops(lst):
    txt = sha256(''.join(lst).encode()).hexdigest()
    txt = ''.join(sorted(txt, key=str.isdigit))
    return sha256(txt.encode()).hexdigest()