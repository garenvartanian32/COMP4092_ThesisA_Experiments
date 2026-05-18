def is_palindrome(p):
    p = ''.join(i for i in p.lower() if i.isalpha())
    if len(p) <= 1:
        return True
    else:
        return p[0] == p[-1] and is_palindrome(p[1:-1])