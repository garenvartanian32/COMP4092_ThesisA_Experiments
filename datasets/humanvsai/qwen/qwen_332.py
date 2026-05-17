def vocalized_similarity(word1, word2):
    harakat = set(['َ', 'ِ', 'ُ', 'ً', 'ٍ', 'ٌ', 'ْ'])
    base_word1 = ''.join([char for char in word1 if char not in harakat])
    base_word2 = ''.join([char for char in word2 if char not in harakat])
    if base_word1 != base_word2:
        return False
    harakat_errors = 0
    (i, j) = (0, 0)
    while i < len(word1) and j < len(word2):
        if word1[i] in harakat and word2[j] in harakat:
            if word1[i] != word2[j]:
                harakat_errors += 1
            i += 1
            j += 1
        elif word1[i] in harakat:
            harakat_errors += 1
            i += 1
        elif word2[j] in harakat:
            harakat_errors += 1
            j += 1
        else:
            i += 1
            j += 1
    if harakat_errors == 0:
        return True
    else:
        return -harakat_errors
word1 = u'مَسْتَشَرَ'
word2 = u'مَسْتَشَرَ'