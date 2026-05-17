def gather_hinting(config, rules, valid_paths):
    hint_args = []
    for rule in rules:
        if rule['type'] == 'path':
            path = rule['value']
            if path in valid_paths:
                hint_args.append(path)
        elif rule['type'] == 'tag':
            tag = rule['value']
            hint_args.append(tag)
        elif rule['type'] == 'user':
            user = rule['value']
            hint_args.append(user)
        elif rule['type'] == 'date':
            date = rule['value']
            hint_args.append(date)
        elif rule['type'] == 'event':
            event = rule['value']
            hint_args.append(event)
        elif rule['type'] == 'category':
            category = rule['value']
            hint_args.append(category)
        elif rule['type'] == 'severity':
            severity = rule['value']
            hint_args.append(severity)
        elif rule['type'] == 'source':
            source = rule['value']
            hint_args.append(source)
        elif rule['type'] == 'destination':
            destination = rule['value']
            hint_args.append(destination)
    return hint_args