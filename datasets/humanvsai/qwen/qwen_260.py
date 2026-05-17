def previous(self, type=None):
    if type is None:
        return self._previous_word()
    else:
        return self._previous_word_of_type(type)

def _previous_word(self):
    """Returns the previous word in the sentence."""
    pass

def _previous_word_of_type(self, type):
    """Returns the previous word in the sentence of the given type."""
    pass