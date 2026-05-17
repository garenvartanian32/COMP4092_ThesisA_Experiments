import ctypes

def win_set_trans(title, trans):
    """Sets the transparency of a window.
    :param title: The title of the window.
    :param trans: A number in the range 0 - 255. The larger the number,
        the more transparent the window will become.
    :return:"""

    # Load the DLL
    user32 = ctypes.WinDLL('user32')

    # Get the handle of the window
    hwnd = user32.FindWindowW(None, title)

    # Set the window's transparency
    user32.SetLayeredWindowAttributes(hwnd, 0, trans, 2)