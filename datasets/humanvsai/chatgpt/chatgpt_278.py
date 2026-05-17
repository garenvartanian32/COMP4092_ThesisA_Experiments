def slice_indices(fdmt_state, dm):
    """
    Given FDMT state, return indices to slice partial FDMT solution and sump to a given DM.
    :param fdmt_state: FDMT state to be partially sliced and sump to a given DM.
    :param dm: DM to slice the FDMT state at.
    :return: A tuple containing the indices to slice the FDMT state and the sump, respectively.
    """
    indices = [i for i in range(len(fdmt_state[0])) if fdmt_state[0][i] <= dm]
    sump_index = min((i for i in range(len(fdmt_state[1])) if fdmt_state[1][i] > dm), default=len(fdmt_state[1]))
    return tuple([indices, sump_index])
