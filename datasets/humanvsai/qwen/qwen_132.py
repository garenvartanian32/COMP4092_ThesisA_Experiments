def save_file(f, full_path):
    with open(full_path, 'wb') as file:
        file.write(f.read())
    os.chmod(full_path, 420)

def load_file(full_path):
    """Loads file from full_path."""
    with open(full_path, 'rb') as file:
        return file.read()

def main():
    file_content = b'Hello, world!'
    file_path = 'example.txt'
    save_file(io.BytesIO(file_content), file_path)
    loaded_content = load_file(file_path)
    print(loaded_content)