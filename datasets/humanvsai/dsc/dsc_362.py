import cv2

def imread(img, color=None, dtype=None):
    if color is None:
        color = cv2.IMREAD_UNCHANGED
    img = cv2.imread(img, color)
    if dtype is not None:
        img = img.astype(dtype)
    return img