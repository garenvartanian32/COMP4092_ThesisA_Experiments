def _update_structure_from_config(self, structure):
    for (key, value) in structure.items():
        if isinstance(value, dict):
            self._update_structure_from_config(value)
        elif isinstance(value, str):
            structure[key] = self._get_updated_path(value)
        else:
            raise ValueError(f'Unsupported type {type(value)} for key {key}')

def _get_updated_path(self, path):
    """Get the updated path based on the configuration.

        :param path: The original path.
        :type path: str
        :return: The updated path.
        :rtype: str"""
    return path