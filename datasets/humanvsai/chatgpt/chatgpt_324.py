def construct_hint_arguments(rules):
    hint_args = []
    for rule in rules:
        hint_args.append(f"--hint={rule}")
    return hint_args
