import ctypes

def _get_win_folder_from_registry(csidl_name):
    """This is a fallback technique at best. I'm not sure if using the
    registry for this guarantees us the correct answer for all CSIDL_*
    names."""
    # Load the shell32.dll library
    shell32 = ctypes.windll.shell32

    # Create a buffer to store the path
    path_buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)

    # Call the function to get the folder path
    shell32.SHGetFolderPathW(None, csidl_name, None, 0, path_buf)

    # Return the path
    return path_buf.value

# Use the function
print(_get_win_folder_from_registry(36))  # CSIDL_PROGRAM_FILESX86