def _update_structure_from_config(self, structure, config):
    """Update the paths according to configs.

    :param structure: The read structure.
    :type structure: dict
    :param config: The configuration.
    :type config: dict
    """
    for path, value in config.items():
        # Split the path into its components
        path = path.split('.')

        # Navigate to the correct node in the structure
        node = structure
        for key in path[:-1]:
            node = node[key]

        # Update the value
        node[path[-1]] = value