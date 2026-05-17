def win_set_trans(title, trans, **kwargs):
    import win32gui
    import win32con
    hwnd = win32gui.FindWindow(None, title)
    if hwnd:
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        style |= win32con.WS_EX_LAYERED
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, style)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, trans, win32con.LWA_ALPHA)
    else:
        print(f"Window with title '{title}' not found.")