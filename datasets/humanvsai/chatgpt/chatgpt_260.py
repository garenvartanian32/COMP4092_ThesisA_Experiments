def prev_word(sentence: str, word_type: str) -> str:
    words = sentence.split()
    prev_word = None
    for i, word in enumerate(words):
        if i > 0 and words[i-1] == prev_word:
            prev_word = word
            continue
        if word.endswith(",") or word.endswith("."):
            word = word[:-1]
        if word_type in ("noun", "verb", "adverb", "adjective"):
            if word_type == "noun":
                if word.lower() in ("a", "an", "the"):
                    continue
                elif word.lower().endswith("s'"):
                    word = word[:-2]
                    word_type = "plural"
            if word_type == "adverb":
                word_type = "adjective"
            if word_type == "adjective":
                if word.lower() in ("very", "quite", "rather", "too"):
                    continue
                elif word.lower().endswith("ly"):
                    continue
            if word_type in ("verb", "adjective"):
                if word.lower().endswith("ing"):
                    word = word[:-3]
                    if word_type == "verb":
                        word_type = "gerund"
                    else:
                        word_type = "adjective"
            if word_type.lower() == word.lower():
                prev_word = word
                continue
        prev_word = None
    return prev_word or ""