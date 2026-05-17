def syllabify(self, word):
        prefixes = self.language['single_syllable_prefixes']
        prefixes.sort(key=len, reverse=True)
        # Check if word is in exception dictionary
        if word in self.language['exceptions']:
            syllables = self.language['exceptions'][word]
        # Else, breakdown syllables for word
        else:
            syllables = []
            # Remove prefixes
            for prefix in prefixes:
                if word.startswith(prefix):
                    syllables.append(prefix)
                    word = re.sub('^%s' % prefix, '', word)
                    break
            # Initialize syllable to build by iterating through over characters
            syllable = ''
            # Get word length for determining character position in word
            word_len = len(word)
            # Iterate over characters to build syllables
            for i, char in enumerate(word):
                # Build syllable
                syllable = syllable + char
                syllable_complete = False
                # Checks to process syllable logic
                char_is_vowel = self._is_vowel(char)
                has_next_char = i < word_len - 1
                has_prev_char = i > 0
                # If it's the end of the word, the syllable is complete
                if not has_next_char:
                    syllable_complete = True
                else:
                    next_char = word[i + 1]
                    if has_prev_char:
                        prev_char = word[i - 1]
                    # 'i' is a special case for a vowel. when i is at the 
                    # beginning of the word (Iesu) or i is between 
                    # vowels (alleluia), then the i is treated as a 
                    # consonant (y) Note: what about compounds like 'adiungere'
                    if char == 'i' and has_next_char and self._is_vowel(next_char): 
                        if i == 0:
                            char_is_vowel = False
                        elif self._is_vowel(prev_char):
                            char_is_vowel = False
                    # Determine if the syllable is complete
                    if char_is_vowel:
                        if (
                                    (  # If the next character's a vowel
                                       self._is_vowel(
                                               next_char)  # And it doesn't compose a dipthong with the current character
                                       and not self._is_diphthong(char,
                                                                  next_char)  # And the current character isn't preceded by a q, unless followed by a u
                                       and not (
                                                           has_prev_char
                                                       and prev_char == "q"
                                                   and char == "u"
                                               and next_char != "u"
                                       )
                                       )
                                or (
                                        # If the next character's a consonant but not a double consonant, unless it's a mute consonant followed by a liquid consonant
                                        i < word_len - 2
                                        and (
                                                        (
                                                                    (
                                                                                        has_prev_char
                                                                                    and prev_char != "q"
                                                                                and char == "u"
                                                                            and self._is_vowel(word[i + 2])
                                                                    )
                                                                or (
                                                                                not has_prev_char
                                                                            and char == "u"
                                                                        and self._is_vowel(word[i + 2])
                                                                )
                                                        )
                                                    or (
                                                                        char != "u"
                                                                and self._is_vowel(word[i + 2])
                                                            and not self._is_diphthong(char, next_char)
                                                    )
                                                or (
                                                            self._is_mute_consonant_or_f(next_char)
                                                        and self._is_liquid_consonant(word[i + 2])
                                                )
                                        )
                                )
                        ):
                            syllable_complete = True
                    # Otherwise, it's a consonant
                    else:
                        if (  # If the next character's also a consonant (but it's not the last in the word)
                              (
                                          not self._is_vowel(next_char)
                                      and i < word_len - 2
                              )  # If the char's not a mute consonant followed by a liquid consonant
                              and not (
                                          self._is_mute_consonant_or_f(char)
                                      and self._is_liquid_consonant(next_char)
                              )  # If the char's not a c, p, or t followed by an h
                              and not (
                                          (
                                                              has_prev_char
                                                          and not self._is_vowel(prev_char)
                                                      and char in ['c', 'p', 't'] and next_char == 'h'
                                          )
                                      or (
                                                      not has_prev_char
                                                  and char in ['c', 'p', 't'] and next_char == 'h'
                                      )
                              )  # And it's not the only letter in the syllable
                              and not len(syllable) == 1
                              ):
                            syllable_complete = True
                # If it's a complete syllable, append it to syllables list and reset syllable
                if syllable_complete:
                    syllables.append(syllable)
                    syllable = ''
        return syllables