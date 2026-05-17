def validate(parsed_args):
    dataset = read_dataset(parsed_args.dataset_file)
    config = read_config(parsed_args.config_file)
    validation_results = validate_dataset(dataset, config)
    unsuccessful_expectations = count_unsuccessful_expectations(validation_results)
    return unsuccessful_expectations

def read_dataset(file_path):
    """Reads a dataset from a file.

    :param file_path: The path to the dataset file.
    :return: The dataset as a pandas DataFrame.
    """
    import pandas as pd
    return pd.read_csv(file_path)

def read_config(file_path):
    """Reads a configuration from a file.

    :param file_path: The path to the configuration file.
    :return: The configuration as a dictionary.
    """
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def validate_dataset(dataset, config):
    """Validates a dataset against a configuration.

    :param dataset: The dataset as a pandas DataFrame.
    :param config: The configuration as a dictionary.
    :return: A list of validation results.
    """
    validation_results = []
    for expectation in config['expectations']:
        result = check_expectation(dataset, expectation)
        validation_results.append(result)
    return validation_results

def check_expectation(dataset, expectation):
    """Checks a single expectation against the dataset.

    :param dataset: The dataset as a pandas DataFrame.
    :param expectation: The expectation as a dictionary.
    :return: A dictionary containing the result of the expectation check.
    """
    column = expectation['column']
    condition = expectation['condition']
    if condition == 'not_null':
        result = dataset[column].notnull().all()
    elif condition == 'unique':
        result = dataset[column].is_unique
    elif condition == 'type':
        expected_type = expectation['type']
        result = dataset[column].dtype == expected_type
    else:
        result = False