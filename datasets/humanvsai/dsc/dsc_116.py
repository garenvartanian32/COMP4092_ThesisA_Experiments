import os

class DirectoryParser:
    def __init__(self, directory):
        self.directory = directory

    def parsing(self):
        for root, dirs, files in os.walk(self.directory):
            print(f"Root: {root}")
            print(f"Directories: {dirs}")
            print(f"Files: {files}")
            print("-------------------")

# Usage
parser = DirectoryParser('/path/to/directory')
parser.parsing()