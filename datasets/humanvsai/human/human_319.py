def truncation_selection(random, population, args):
    num_selected = args.setdefault('num_selected', len(population))
    population.sort(reverse=True)
    return population[:num_selected]