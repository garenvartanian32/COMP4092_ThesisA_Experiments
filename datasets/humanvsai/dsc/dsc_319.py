def truncation_selection(random, population, args):
    """Selects the best individuals from the population.
    
    This function performs truncation selection, which means that only
    the best individuals from the current population are selected. This
    is a completely deterministic selection mechanism.
    
    .. Arguments:
       random -- the random number generator object
       population -- the population of individuals
       args -- a dictionary of keyword arguments

    Optional keyword arguments in args:
    
    - *num_selected* -- the number of individuals to be selected 
      (default len(population))"""

    # Get the number of individuals to be selected
    num_selected = args.get('num_selected', len(population))

    # Sort the population by fitness
    population.sort(key=lambda x: x.fitness)

    # Select the best individuals
    selected = population[-num_selected:]

    return selected