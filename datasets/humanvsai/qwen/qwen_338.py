def count_characters(root, out):
    if root is None:
        return
    if root.is_file():
        with open(root, 'r') as file:
            for line in file:
                for char in line:
                    if char in out:
                        out[char] += 1
                    else:
                        out[char] = 1
    elif root.is_dir():
        for child in root.iterdir():
            count_characters(child, out)