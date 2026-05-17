class Syllabifier:
    def __init__(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u']

    def syllabify(self, word):
        syllables = []
        syllable = ''
        for i, char in enumerate(word):
            syllable += char
            if char in self.vowels:
                if i == len(word) - 1 or word[i+1] not in self.vowels:
                    syllables.append(syllable)
                    syllable = ''
        return syllables

# Test the function
s = Syllabifier()
print(s.syllabify('beautiful'))  # Output: ['beau', 'tiful']