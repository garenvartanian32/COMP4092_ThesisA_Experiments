import winreg

def fallback_csidl_name_to_id(name):
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                          "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders")
    try:
        result, _ = winreg.QueryValueEx(key, name)
        return result
    except Exception:
        return None
