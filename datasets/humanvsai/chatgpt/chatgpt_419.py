from scipy.sparse import csgraph

def is_ergodic(T, tol=1e-8):
    num_components, _ = csgraph.connected_components(T, directed=True)
    return num_components == 1
