def gather_hinting(config, rules, valid_paths):
    hinting = collections.defaultdict(list)
    for rule in rules:
        root, name = rule.code_path.split(':', 1)
        info = valid_paths[root][name]
        if info['hints-callable']:
            # Call the callable hint to get its values
            result = info['hints-callable'](config=config, **rule.arguments)
            # If the rule is inverted, but the hint is not invertible, then
            # there is no hinting we can provide.  Carry on.
            if rule.negated and not info['hints-invertible']:
                continue
            for key, values in result.items():
                # Negate the hint if necessary
                key = 'not_' + key if rule.negated else key
                hinting[key].extend(values)
        # Then, finish off with all the other ordinary, non-callable hints
        for key, value in info['datanommer-hints'].items():
            # If the rule is inverted, but the hint is not invertible, then
            # there is no hinting we can provide.  Carry on.
            if rule.negated and not info['hints-invertible']:
                continue
            # Otherwise, construct the inverse hint if necessary
            key = 'not_' + key if rule.negated else key
            # And tack it on.
            hinting[key] += value
    log.debug('gathered hinting %r', hinting)
    return hinting