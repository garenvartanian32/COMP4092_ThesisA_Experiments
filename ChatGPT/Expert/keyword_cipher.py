def keyword_cipher(message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = ""

    for char in keyword.lower():
        if char.isalpha() and char not in key:
            key += char

    for char in alphabet:
        if char not in key:
            key += char

    encrypted = []

    for char in message:
        lower = char.lower()

        if lower in alphabet:
            index = alphabet.index(lower)
            cipher_char = key[index]

            if char.isupper():
                encrypted.append(cipher_char.upper())
            else:
                encrypted.append(cipher_char)
        else:
            encrypted.append(char)

    return "".join(encrypted)
