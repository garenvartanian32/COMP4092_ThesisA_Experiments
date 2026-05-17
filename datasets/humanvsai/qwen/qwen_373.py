def _included_frames(frame_list, frame_format):
    included_frames = []
    for frame in frame_list:
        if frame_format in frame:
            included_frames.append(frame)
    return included_frames

def _excluded_frames(frame_list, frame_format):
    """frame_list should be a list of filenames"""
    excluded_frames = []
    for frame in frame_list:
        if frame_format not in frame:
            excluded_frames.append(frame)
    return excluded_frames

def filter_frames(frame_list, frame_format, include=True):
    """Filter frames based on the frame_format.

    Args:
        frame_list (list): A list of filenames.
        frame_format (str): The format to filter frames by.
        include (bool): If True, include frames with the frame_format; if False, exclude them.

    Returns:
        list: A list of filtered filenames.
    """
    if include:
        return _included_frames(frame_list, frame_format)
    else:
        return _excluded_frames(frame_list, frame_format)
frame_list = ['frame001.jpg', 'frame002.png', 'frame003.jpg', 'frame004.bmp']
frame_format = '.jpg'
filtered_frames = filter_frames(frame_list, frame_format, include=True)