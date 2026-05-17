def get_experiments(base, load=False):
    experiments = find_directories(base)
    valid_experiments = [e for e in experiments if validate(e,cleanup=False)]
    bot.info("Found %s valid experiments" %(len(valid_experiments)))
    if load is True:
        valid_experiments = load_experiments(valid_experiments)
    #TODO at some point in this workflow we would want to grab instructions from help
    # and variables from labels, environment, etc.
    return valid_experiments