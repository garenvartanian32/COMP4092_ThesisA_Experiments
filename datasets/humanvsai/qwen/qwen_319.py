def truncation_selection(random, population, args):
    num_selected = args.get('num_selected', len(population))
    sorted_population = sorted(population, key=lambda x: x.fitness, reverse=True)
    selected_population = sorted_population[:num_selected]
    return selected_population