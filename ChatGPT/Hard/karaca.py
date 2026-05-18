def encrypt(word):
    replacements = {
        "a": "0",
        "e": "1",
        "i": "2",
        "o": "2",
        "u": "3"
    }

    encrypted = ""

    for char in word[::-1]:
        encrypted += replacements.get(char, char)

    return encrypted + "aca"
