import docker

class SwarmManager:
    def __init__(self, client):
        self.client = client

    def leave_swarm(self, force=False):
        """Leave a swarm.

        Args:
            force (bool): Leave the swarm even if this node is a manager.
                Default: ``False``

        Returns:
            ``True`` if the request went through.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        try:
            if force:
                self.client.leave_swarm(force=True)
            else:
                self.client.leave_swarm()
            return True
        except docker.errors.APIError as e:
            print(f"An error occurred: {e}")
            raise