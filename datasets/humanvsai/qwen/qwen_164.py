def leave_swarm(self, force=False):
    try:
        self.client.leave_swarm(force=force)
        return True
    except docker.errors.APIError as e:
        raise docker.errors.APIError(f'Failed to leave swarm: {e}')

def join_swarm(self, join_token, advertise_addr=None, listen_addr='0.0.0.0:2377', remote_addrs=None, join_condition='acceptance', data_path_addr=None):
    """Join a swarm.

        Args:
            join_token (str): Swarm join token.
            advertise_addr (str): Externally reachable address advertised to other nodes.
                Default: ``None``
            listen_addr (str): Listen address used for inter-manager communication.
                Default: ``'0.0.0.0:2377'``
            remote_addrs (list): Addresses of manager nodes to connect to.
                Default: ``None``
            join_condition (str): Condition for joining the swarm.
                Default: ``'acceptance'``
            data_path_addr (str): Address or interface to use for data path traffic.
                Default: ``None``

        Returns:
            ``True`` if the request went through.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error."""
    try:
        self.client.join_swarm(join_token=join_token, advertise_addr=advertise_addr, listen_addr=listen_addr, remote_addrs=remote_addrs, join_condition=join_condition, data_path_addr=data_path_addr)
        return True
    except docker.errors.APIError as e:
        raise docker.errors.APIError(f'Failed to join swarm: {e}')