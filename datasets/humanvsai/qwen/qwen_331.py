def get_texts(self):
    with open(self.file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tokens = line.strip().split()
            filtered_tokens = [token for token in tokens if self.filter_token(token)]
            yield filtered_tokens

def filter_token(self, token):
    """Filter tokens based on certain criteria"""
    return 3 <= len(token) <= 10
file_path = 'documents.txt'
texts = get_texts(file_path)