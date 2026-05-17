import json

def validate_dataset(parsed_args):
    with open(parsed_args.dataset_file, 'r') as f:
        dataset = json.load(f)
    with open(parsed_args.config_file, 'r') as f:
        config = json.load(f)
    unsuccessful_expectations = 0
    for expectation in config:
        if expectation['type'] == 'min_length':
            if len(dataset[expectation['field']]) < expectation['value']:
                unsuccessful_expectations += 1
        elif expectation['type'] == 'max_length':
            if len(dataset[expectation['field']]) > expectation['value']:
                unsuccessful_expectations += 1
        elif expectation['type'] == 'exact_length':
            if len(dataset[expectation['field']]) != expectation['value']:
                unsuccessful_expectations += 1
        elif expectation['type'] == 'not_null':
            if dataset[expectation['field']] is None:
                unsuccessful_expectations += 1
    return unsuccessful_expectations
