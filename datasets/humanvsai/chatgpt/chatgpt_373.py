def validate_frame_list(frame_list):
    if not isinstance(frame_list, list):
        raise TypeError("frame_list must be a list")
    for file_name in frame_list:
        if not isinstance(file_name, str):
            raise TypeError("all items in frame_list must be strings")
    return True
