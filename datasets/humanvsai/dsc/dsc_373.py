def _included_frames(frame_list, frame_format):
    """
    frame_list should be a list of filenames
    frame_format should be a string representing the format of the frames
    """
    for frame in frame_list:
        if not frame.endswith(frame_format):
            return False
    return True