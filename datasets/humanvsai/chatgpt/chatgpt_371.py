def validate_config(config_path, control_socket_path, pid_file_path):
    if not config_path or not control_socket_path or not pid_file_path:
        raise ValueError("Missing configuration file path, control socket file path, and/or pid file path")
