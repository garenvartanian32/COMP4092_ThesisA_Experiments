def get_active_services():
    import win32serviceutil
    import win32service
    import win32con
    services = []
    scm_handle = win32service.OpenSCManager(None, None, win32service.SC_MANAGER_ENUMERATE_SERVICE)
    try:
        type_filter = win32service.SERVICE_WIN32_OWN_PROCESS | win32service.SERVICE_WIN32_SHARE_PROCESS
        state_filter = win32service.SERVICE_STATE_ALL
        status_handle = win32service.EnumServicesStatusEx(scm_handle, win32service.SC_ENUM_PROCESS_INFO, type_filter, state_filter)
        for service in status_handle:
            if service[1] == win32service.SERVICE_RUNNING:
                services.append(service)
    finally:
        win32service.CloseServiceHandle(scm_handle)
    return services