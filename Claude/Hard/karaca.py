def encrypt(word):
    # Step 1 — reverse
    word = word[::-1]
 
    # Step 2 — shift each letter forward by 1 (z wraps to a)
    shifted = []
    for ch in word:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            shifted.append(chr(base + (ord(ch) - base + 1) % 26))
        else:
            shifted.append(ch)
 
    # Step 3 — capitalise odd indices
    return ''.join(
        ch.upper() if i % 2 != 0 else ch.lower()
        for i, ch in enumerate(shifted)
    )