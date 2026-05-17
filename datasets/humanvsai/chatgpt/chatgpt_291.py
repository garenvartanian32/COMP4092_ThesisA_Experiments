def update_paths(structure):
    for key in structure:
        if isinstance(structure[key], dict):
            update_paths(structure[key])
        elif isinstance(structure[key], str):
            if structure[key].startswith('$'):
                config_key = structure[key][1:]
                if config_key in config:
                    structure[key] = config[config_key]
                else:
                    raise ValueError(f"Config value for {config_key} not found")
    return structure
