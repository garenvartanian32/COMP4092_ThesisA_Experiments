def trim_phonetics(root):
    import re
    phonetic_pattern = re.compile('\\{[^}]*\\}')
    trimmed_string = phonetic_pattern.sub('', root)
    return trimmed_string
example_string = 'This is an example {phonetic: markup} string.'
trimmed_string = trim_phonetics(example_string)