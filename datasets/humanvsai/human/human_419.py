def is_ergodic(T, tol):
    if isdense(T):
        T = T.tocsr()
    if not is_transition_matrix(T, tol):
        raise ValueError("given matrix is not a valid transition matrix.")
    num_components = connected_components(T, directed=True, \
                                          connection='strong', \
                                          return_labels=False)
    return num_components == 1