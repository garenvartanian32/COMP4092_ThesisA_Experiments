def truncation_selection(random, population, args={}):
    num_selected = args.get('num_selected', len(population))
    return sorted(population, key=fitness_key, reverse=True)[:num_selected]
