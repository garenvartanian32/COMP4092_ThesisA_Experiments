def validate_config(cls, config):
    if not config.get('config_file_path'):
        raise ValueError('config_file_path is missing in the configuration.')
    if not config.get('control_socket_file_path'):
        raise ValueError('control_socket_file_path is missing in the configuration.')
    if not config.get('pid_file_path'):
        raise ValueError('pid_file_path is missing in the configuration.')
    return True
config = {'config_file_path': '/etc/haproxy/haproxy.cfg', 'control_socket_file_path': '/var/run/haproxy.sock', 'pid_file_path': '/var/run/haproxy.pid'}