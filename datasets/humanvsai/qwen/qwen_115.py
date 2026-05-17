def get_experiments(base, load=False):
    import os
    import json
    experiments = []
    for (root, dirs, files) in os.walk(base):
        if 'config.json' in files:
            experiment_path = os.path.join(root, 'config.json')
            if load:
                with open(experiment_path, 'r') as f:
                    experiments.append(json.load(f))
            else:
                experiments.append(experiment_path)
    return experiments