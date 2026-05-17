import os
import json

def get_experiments(base, load=False):
    """get_experiments will return loaded json for all valid experiments from an experiment folder
    :param base: full path to the base folder with experiments inside
    :param load: if True, returns a list of loaded config.json objects. If False (default) returns the paths to the experiments"""

    # List to store the results
    results = []

    # Walk through the directory
    for root, dirs, files in os.walk(base):
        # Check if 'config.json' is in the files
        if 'config.json' in files:
            # If load is True, load the json and append to results
            if load:
                with open(os.path.join(root, 'config.json')) as f:
                    results.append(json.load(f))
            # If load is False, append the path to the results
            else:
                results.append(os.path.join(root, 'config.json'))

    return results