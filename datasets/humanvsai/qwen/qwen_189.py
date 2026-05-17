def syllabify(self, word):
    vowels = 'aeiouy'
    syllables = []
    i = 0
    while i < len(word):
        if word[i] in vowels:
            end = i + 1
            while end < len(word) and word[end] not in vowels:
                end += 1
            syllables.append(word[i:end])
            i = end
        else:
            i += 1
    return syllables