def parse_documents(file_path):
    """Parse documents from a .txt file assuming 1 document per line, yielding lists of filtered tokens.

    Args:
        file_path (str): Path to the file containing documents.

    Yields:
        list: List of filtered tokens for each document in the file.

    """

    with open(file_path, 'r') as f:
        for line in f:
            # Remove new line character from the end of line
            line = line.rstrip('\n')
            # Tokenize the line
            tokens = line.split()
            # Filter the tokens
            filtered_tokens = [token for token in tokens if token.isalpha()]
            
            yield filtered_tokens
