import docker

def _build_volume(self, volume):
    """Given a generic volume definition, create the volumes element"""
    client = docker.from_env()
    volume_name = volume['name']
    volume_driver = volume.get('driver', 'local')
    volume_driver_opts = volume.get('driver_opts', {})
    volume_labels = volume.get('labels', {})

    try:
        client.volumes.create(volume_name, driver=volume_driver, driver_opts=volume_driver_opts, labels=volume_labels)
    except docker.errors.APIError as e:
        print(f"Error creating volume: {e}")