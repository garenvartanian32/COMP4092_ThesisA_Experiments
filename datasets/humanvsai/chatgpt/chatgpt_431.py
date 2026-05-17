def calc_unbalanced_charges_and_radicals(atoms):
    """
    Calculate the unbalanced charges and radicals for skin atoms.

    :param atoms: A list of skin atoms.
    :type atoms: list
    :return: A tuple containing the total unbalanced charges and radicals for skin atoms.
    :rtype: tuple
    """

    unbalanced_charges = 0
    radicals = 0

    for atom in atoms:
        if atom['charge'] != 0:
            unbalanced_charges += atom['charge']
        if atom['radical'] != 0:
            radicals += atom['radical']

    return (unbalanced_charges, radicals)
