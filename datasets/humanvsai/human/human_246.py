def probabilities(items, params):
    params = np.asarray(params)
    return softmax(params.take(items))