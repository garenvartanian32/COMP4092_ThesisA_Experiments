def _get_win_folder_from_registry(csidl_name):
    import winreg as reg
    shell_folder_name = {'CSIDL_APPDATA': 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders', 'CSIDL_COMMON_APPDATA': 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders', 'CSIDL_LOCAL_APPDATA': 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders', 'CSIDL_PROGRAM_FILES': 'Software\\Microsoft\\Windows\\CurrentVersion', 'CSIDL_PROGRAM_FILESX86': 'Software\\Microsoft\\Windows\\CurrentVersion', 'CSIDL_SYSTEM': 'Software\\Microsoft\\Windows\\CurrentVersion', 'CSIDL_WINDOWS': 'Software\\Microsoft\\Windows\\CurrentVersion'}
    sub_key = shell_folder_name.get(csidl_name)
    if not sub_key:
        raise ValueError(f'Unknown CSIDL name: {csidl_name}')
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, sub_key)
    try:
        (value, _) = reg.QueryValueEx(key, csidl_name)
    except FileNotFoundError:
        key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, sub_key)
        (value, _) = reg.QueryValueEx(key, csidl_name)
    finally:
        reg.CloseKey(key)
    return value

def get_win_folder(csidl_name):
    """Get the path to a special folder designated by the CSIDL name."""
    import ctypes
    from ctypes import wintypes
    SHGetFolderPath = ctypes.windll.shell32.SHGetFolderPathW
    SHGetFolderPath.argtypes = [wintypes.HWND, ctypes.c_int, wintypes.HANDLE, wintypes.DWORD, wintypes.LPCWSTR]
    SHGetFolderPath.restype = wintypes.HRESULT