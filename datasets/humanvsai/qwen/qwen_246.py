def probabilities(items, params):
    import numpy as np
    items = np.array(items)
    utilities = np.dot(items, params)
    exp_utilities = np.exp(utilities)
    probs = exp_utilities / np.sum(exp_utilities)
    return probs
items = np.array([[1, 2], [3, 4], [5, 6]])
params = np.array([0.5, 0.5])