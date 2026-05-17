def load_yaml(path):
    import yaml
    from collections import OrderedDict

    def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):

        class OrderedLoader(Loader):
            pass

        def construct_mapping(loader, node, deep=False):
            loader.flatten_mapping(node)
            return object_pairs_hook(loader.construct_pairs(node, deep))
        OrderedLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)
        return yaml.load(stream, OrderedLoader)
    with open(path, 'r') as file:
        return ordered_load(file)

def load_json(path):
    """Load JSON file into an ordered dictionary

    Args:
        path (str): Path to JSON file

    Returns:
        OrderedDict: Ordered dictionary containing loaded JSON file"""
    import json
    from collections import OrderedDict
    with open(path, 'r') as file:
        return json.load(file, object_pairs_hook=OrderedDict)

def load_config(path):
    """Load configuration file into an ordered dictionary

    Args:
        path (str): Path to configuration file

    Returns:
        OrderedDict: Ordered dictionary containing loaded configuration file

    Raises:
        ValueError: If the file extension is not supported"""
    if path.endswith('.yaml') or path.endswith('.yml'):
        return load_yaml(path)
    elif path.endswith('.json'):
        return load_json(path)
    else:
        raise ValueError('Unsupported file extension. Please use .yaml, .yml, or .json.')