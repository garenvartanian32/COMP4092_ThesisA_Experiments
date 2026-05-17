def orthologize_context(context, target_species):
    """
    This function orthologizes a given context by replacing the species with the target species.
    It also adds a new annotation type of OrthologizedFrom.

    Parameters:
    context (str): The context string to be orthologized.
    target_species (str): The target species to replace in the context.

    Returns:
    str: The orthologized context string with the new annotation.

    """
    orthologized_context = context.replace("Species", target_species)
    orthologized_context += " [OrthologizedFrom: Species]"
    return orthologized_context
