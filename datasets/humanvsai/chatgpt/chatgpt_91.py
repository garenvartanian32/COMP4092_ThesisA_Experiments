import win32gui

def set_window_transparency(title, trans, **kwargs):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd != 0:
        exstyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, exstyle | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, trans, win32con.LWA_ALPHA)
        return True
    else:
        return False