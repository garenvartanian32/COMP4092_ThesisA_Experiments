import yaml
from collections import OrderedDict

def load_yaml(path):
    """Load YAML file into an ordered dictionary

    Args:
        path (str): Path to YAML file

    Returns:
        OrderedDict: Ordered dictionary containing loaded YAML file
    """
    with open(path, 'r') as stream:
        try:
            return yaml.load(stream, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            print(exc)