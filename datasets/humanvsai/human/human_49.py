def file_variations(filename, extensions):
    (label, ext) = splitext(filename)
    return [label + extention for extention in extensions]