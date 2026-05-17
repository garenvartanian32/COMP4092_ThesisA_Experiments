def are_words_similar(word1, word2):
    # Remove all non-alphabetic characters and convert to lowercase
    word1 = ''.join(filter(str.isalpha, word1)).lower()
    word2 = ''.join(filter(str.isalpha, word2)).lower()
    
    # Check if the two words have the same length
    if len(word1) != len(word2):
        return -1
    
    # Check if the two words are identical
    if word1 == word2:
        return True
    
    # Check if the two words have the same letters and the same harakats
    letters1 = set(word1)
    letters2 = set(word2)
    if letters1 != letters2:
        return -2
    
    harakats1 = set(c for c in word1 if not c.isalpha())
    harakats2 = set(c for c in word2 if not c.isalpha())
    if harakats1 != harakats2:
        return -3
    
    return True
