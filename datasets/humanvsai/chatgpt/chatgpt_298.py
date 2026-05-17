def initialize_biases(input_size, output_size):
    """
    Initializes the biases of the forget gate to 1, and all other gates to 0.

    Args:
    input_size (int): The size of the input layer.
    output_size (int): The size of the output layer.

    Returns:
    biases (ndarray): A 2D numpy array of shape (output_size,). The biases are initialized according to the above rule.
    """
    biases = np.zeros((output_size,))
    biases[input_size:2*output_size] = 1

    return biases
