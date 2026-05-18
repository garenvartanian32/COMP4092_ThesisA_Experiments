def atbash(s):
    result = []
    for c in s:
        if c.isupper():
            result.append(chr(ord('A') + ord('Z') - ord(c)))
        elif c.islower():
            result.append(chr(ord('a') + ord('z') - ord(c)))
        else:
            result.append(c)
    return ''.join(result)