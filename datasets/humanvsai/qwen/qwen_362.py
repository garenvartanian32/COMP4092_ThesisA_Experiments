def imread(img, color=None, dtype=None):
    if dtype is None:
        dtype = 'uint8'
    if color is None:
        color = 'color'
    if dtype == 'noUint':
        dtype = 'uint8'
    if color == 'color':
        img = cv2.imread(img, cv2.IMREAD_COLOR)
    elif color == 'gray':
        img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    elif color == 'unchanged':
        img = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    else:
        raise ValueError("Invalid color mode. Use 'color', 'gray', or 'unchanged'.")
    if dtype == 'uint8':
        img = img.astype(np.uint8)
    elif dtype == 'float':
        img = img.astype(np.float32) / 255.0
    else:
        raise ValueError("Invalid dtype. Use 'uint8' or 'float'.")
    return img