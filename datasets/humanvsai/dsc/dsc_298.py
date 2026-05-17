import torch

def lstm_hidden_bias(tensor):
    """Initialize the biases of the forget gate to 1, and all other gates to 0,
    following Jozefowicz et al., An Empirical Exploration of Recurrent Network Architectures"""

    # Get the size of the tensor
    size = tensor.size(0)

    # Create a tensor of zeros
    bias = torch.zeros(size, dtype=tensor.dtype, device=tensor.device)

    # Set the forget gate bias to 1
    bias[size // 4:size // 2] = 1

    return bias