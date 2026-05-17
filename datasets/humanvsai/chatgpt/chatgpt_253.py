def create_volumes_element(volume_definition):
    volumes = []
    for name, config in volume_definition.items():
        volume = {
            "name": name,
            "config": config
        }
        volumes.append(volume)
    return volumes
