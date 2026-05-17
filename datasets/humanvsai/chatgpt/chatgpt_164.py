import docker

def leave_swarm(force=False):
    client = docker.from_env()
    return client.swarm.leave(force=force)
