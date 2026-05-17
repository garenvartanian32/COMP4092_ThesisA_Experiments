import configparser

def get_set_config_options(config_file_path, section, option, value=None):
    """
    Get and set config options from config file
    :param config_file_path: str - path and filename of config file
    :param section: str - section name in config file
    :param option: str - option name in config file
    :param value: str - (optional) value to set for the given option
    :return: str - value (if getting), None (if setting)
    """
    config = configparser.ConfigParser()
    config.read(config_file_path)
    if value is None:
        return config.get(section, option)
    else:
        config.set(section, option, value)
        with open(config_file_path, 'w') as config_file:
            config.write(config_file)
