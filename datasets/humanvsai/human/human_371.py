def validate_config(cls, config):
        if "config_file" not in config:
            raise ValueError("No config file path given")
        if "socket_file" not in config:
            raise ValueError("No control socket path given")
        if "pid_file" not in config:
            raise ValueError("No PID file path given")
        if "stats" in config and "port" not in config["stats"]:
            raise ValueError("Stats interface defined, but no port given")
        if "proxies" in config:
            cls.validate_proxies_config(config["proxies"])
        return config