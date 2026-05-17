def train(model, dataset, epochs):
    for epoch in range(epochs):
        # Training process
        # Assuming dataset is a list of tuples (input, target)
        for input, target in dataset:
            model.train(input, target)