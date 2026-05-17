def load_yaml(path):
    # type: (str) -> OrderedDict
    with open(path, 'rt') as f:
        yamldict = yaml.load(f.read(), Loader=yamlloader.ordereddict.CSafeLoader)
    if not yamldict:
        raise (LoadError('YAML file: %s is empty!' % path))
    return yamldict