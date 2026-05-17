import numpy as np

def compute_comparison_probabilities(items, params):
    num_items = len(items)
    probs = np.zeros(num_items)
    for i in range(num_items):
        for j in range(num_items):
            if i == j:
                continue
            diff = params[items[i]] - params[items[j]]
            probs[i] += 1 / (1 + np.exp(-diff))
    probs /= np.sum(probs)
    return probs
