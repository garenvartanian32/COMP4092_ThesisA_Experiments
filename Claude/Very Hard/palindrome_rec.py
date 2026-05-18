def palindrome_phrase(phrase):
    cleaned = ''.join(ch.lower() for ch in phrase if ch.isalnum())
 
    def _check(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return _check(s[1:-1])
 
    return _check(cleaned)