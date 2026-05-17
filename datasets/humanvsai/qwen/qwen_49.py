def file_variations(filename, extensions):
    (base_name, current_ext) = filename.rsplit('.', 1)
    variations = [f'{base_name}.{ext}' for ext in extensions]
    return variations
filename = 'example.txt'
extensions = ['jpg', 'png', 'gif']