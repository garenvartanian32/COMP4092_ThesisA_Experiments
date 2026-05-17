def gather_hinting(config, rules, valid_paths):
    hint_args = []
    for rule in rules:
        if rule in valid_paths:
            hint_args.append(config[rule])
    return hint_args