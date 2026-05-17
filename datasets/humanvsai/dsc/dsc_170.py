import psutil

def get_active_services():
    """Retrieve a list of all active system services."""
    services = []
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] is not None:
            services.append(proc.info['name'])
    return services