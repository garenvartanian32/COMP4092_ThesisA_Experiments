import win32service
import win32serviceutil

def get_active_services():
    return win32serviceutil.EnumServicesStatusEx()[0]
