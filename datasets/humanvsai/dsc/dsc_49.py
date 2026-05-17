import os

def file_variations(filename, extensions):
    # Get the base name of the file (without extension)
    base_name = os.path.splitext(filename)[0]

    # Generate variations
    variations = [base_name + '.' + ext for ext in extensions]

    return variations