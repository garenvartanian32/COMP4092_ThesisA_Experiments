import json

def validate(parsed_args):
    # Load the dataset file
    with open(parsed_args.dataset_file, 'r') as f:
        dataset = json.load(f)

    # Load the config file
    with open(parsed_args.config_file, 'r') as f:
        config = json.load(f)

    # Validate the dataset using the config
    unsuccessful_expectations = 0
    for key, value in config.items():
        if key not in dataset or dataset[key] != value:
            unsuccessful_expectations += 1

    return unsuccessful_expectations