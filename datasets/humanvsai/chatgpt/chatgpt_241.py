def train_epochs(trainset, model, num_epochs):
    for epoch in range(num_epochs):
        for data in trainset:
            inputs, labels = data
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
    print("Training is complete!")
