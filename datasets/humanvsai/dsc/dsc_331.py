import re

def get_texts(self):
    with open('documents.txt', 'r') as f:
        for line in f:
            # Tokenize the line
            tokens = line.split()
            # Filter out non-alphanumeric tokens
            tokens = [token for token in tokens if re.match(r'\w+', token)]
            yield tokens