import os

def iter_regions(self):
    for root, dirs, files in os.walk("path_to_your_directory"):
        for file in files:
            if file.endswith(".region"):  # assuming region files end with .region
                yield os.path.join(root, file)