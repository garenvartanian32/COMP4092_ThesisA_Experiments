def _get_resources(rtype='resources'):
    pass

def _get_resources_summary():
    """Returns a summary of all resource types.

    :return: A dictionary with keys as resource types and values as resources(cpu,mem)
    :rtype: dict
    """
    pass

def _get_resources_by_role(role):
    """Returns resources for a specific role.

    :param role: the name of the role
    :type role: str

    :return: resources(cpu,mem)
    :rtype: Resources
    """
    pass

def _get_resources_by_type_and_role(rtype, role):
    """Returns resources for a specific type and role.

    :param rtype: the type of resources to return
    :type rtype: str
    :param role: the name of the role
    :type role: str

    :return: resources(cpu,mem)
    :rtype: Resources
    """
    pass

def _get_resources_by_type_and_role_summary(rtype, role):
    """Returns a summary of resources for a specific type and role.

    :param rtype: the type of resources to return
    :type rtype: str
    :param role: the name of the role
    :type role: str

    :return: A dictionary with keys as resource types and values as resources(cpu,mem)
    :rtype: dict
    """
    pass

def _get_resources_by_type_summary(rtype):
    """Returns a summary of resources for a specific type.

    :param rtype: the type of resources to return
    :type rtype: str

    :return: A dictionary with keys as resource types and values as resources(cpu,mem)
    :rtype: dict
    """