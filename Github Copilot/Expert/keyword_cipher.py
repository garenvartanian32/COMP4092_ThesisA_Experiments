import string

alphabet = string.ascii_lowercase

def keyword_cipher(key, message):
    # Build the key string
    seen = set()
    key_unique = []
    for c in key.lower():
        if c not in seen and c in alphabet:
            seen.add(c)
            key_unique.append(c)
    rest = [c for c in alphabet if c not in seen]
    key_string = key_unique + rest
    
    # Mapping
    mapping = {alphabet[i]: key_string[i] for i in range(26)}
    
    # Encrypt
    result = []
    for c in message:
        if c.isalpha():
            index = ord(c.lower()) - ord('a')
            new_c = mapping[alphabet[index]]
            if c.isupper():
                new_c = new_c.upper()
            result.append(new_c)
        else:
            result.append(c)
    return ''.join(result)