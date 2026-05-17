import os

def validate_config(config):
    """Validates that a config file path and a control socket file path
        and pid file path are all present in the HAProxy config."""

    # Check if the config file exists
    if not os.path.isfile(config['config_file']):
        raise Exception('Config file does not exist')

    # Check if the control socket file exists
    if not os.path.isfile(config['control_socket']):
        raise Exception('Control socket file does not exist')

    # Check if the pid file exists
    if not os.path.isfile(config['pid_file']):
        raise Exception('PID file does not exist')

    return True