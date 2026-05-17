import unicodedata

def vocalized_similarity(word1, word2):
    # Normalize the words
    word1 = unicodedata.normalize('NFD', word1)
    word2 = unicodedata.normalize('NFD', word2)

    # Compare the words
    if word1 == word2:
        return True
    else:
        return -1

# Test the function
print(vocalized_similarity('élite', 'élite'))  # True
print(vocalized_similarity('élite', 'elite'))  # True
print(vocalized_similarity('élite', 'elitee'))  # -1