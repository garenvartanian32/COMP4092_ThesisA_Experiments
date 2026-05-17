class Resources:
    def __init__(self, cpu, mem):
        self.cpu = cpu
        self.mem = mem

def _get_resources(rtype='resources'):
    """resource types from state summary include:  resources, used_resources
    offered_resources, reserved_resources, unreserved_resources
    The default is resources.

    :param rtype: the type of resources to return
    :type rtype: str
    :param role: the name of the role if for reserved and if None all reserved
    :type rtype: str

    :return: resources(cpu,mem)
    :rtype: Resources"""

    # Here you would implement the logic to get the resources based on the rtype
    # For now, let's just return a dummy Resources object
    return Resources(100, 200)