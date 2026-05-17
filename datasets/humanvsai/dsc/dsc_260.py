class Sentence:
    def __init__(self, sentence):
        self.words = sentence.split()
        self.index = len(self.words)

    def previous(self, type=None):
        self.index -= 1
        if self.index < 0:
            return None
        word = self.words[self.index]
        if type is None or word.type == type:
            return word
        return self.previous(type)