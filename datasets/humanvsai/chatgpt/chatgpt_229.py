from collections import OrderedDict
import yaml

def load_yaml_to_ordered_dict(path: str) -> OrderedDict:
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
        return OrderedDict(data)
