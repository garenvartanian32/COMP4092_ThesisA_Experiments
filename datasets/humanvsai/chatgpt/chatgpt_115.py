import os
import json

def get_experiments(base: str, load: bool = False):
    experiments = []
    for path, folders, files in os.walk(base):
        if 'config.json' in files:
            with open(os.path.join(path, 'config.json')) as f:
                try:
                    experiment = json.load(f)
                    if load:
                        experiments.append(experiment)
                    else:
                        experiments.append(path)
                except json.decoder.JSONDecodeError:
                    pass
    return experiments
