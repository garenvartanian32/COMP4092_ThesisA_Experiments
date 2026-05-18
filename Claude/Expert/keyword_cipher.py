def keyword_cipher(message, keyword):
    keyword_clean = keyword.lower()
 
    # Build cipher alphabet
    seen = set()
    cipher_alpha = []
    for ch in keyword_clean:
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            cipher_alpha.append(ch)
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        if ch not in seen:
            cipher_alpha.append(ch)
 
    # Mapping: plain letter → cipher letter
    mapping = {chr(ord('a') + i): cipher_alpha[i] for i in range(26)}
 
    result = []
    for ch in message.lower():
        result.append(mapping[ch] if ch.isalpha() else ch)
    return ''.join(result)