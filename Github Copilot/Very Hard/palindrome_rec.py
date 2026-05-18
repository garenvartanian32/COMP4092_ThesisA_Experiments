def clean(s):
    return ''.join(c.lower() for c in s if c.isalpha())

def is_palindrome(s):
    cleaned = clean(s)
    return is_palindrome_helper(cleaned)

def is_palindrome_helper(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_helper(s[1:-1])