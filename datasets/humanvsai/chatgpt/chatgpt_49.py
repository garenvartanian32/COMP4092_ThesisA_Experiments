def generate_variations(filename, extensions):
    variations = []
    for extension in extensions:
        variations.append(filename.replace(filename.split('.')[-1], extension))
    return variations
