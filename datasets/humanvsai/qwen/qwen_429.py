def input_size(self):
    return self._input_size

def output_size(self):
    """Size of layer output."""
    return self._output_size

def forward(self, x):
    """Forward pass of the layer."""
    raise NotImplementedError('Subclasses should implement this method.')

def backward(self, grad_output):
    """Backward pass of the layer."""
    raise NotImplementedError('Subclasses should implement this method.')

def __init__(self, input_size, output_size):
    """Initialize the layer with input and output sizes."""
    self._input_size = input_size
    self._output_size = output_size