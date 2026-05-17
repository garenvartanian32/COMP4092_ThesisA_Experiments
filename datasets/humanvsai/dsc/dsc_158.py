import tensorflow as tf

def _reduction_output_shape(x, output_shape, reduced_dim):
    """Helper function to reduce_sum, etc."""
    # Get the shape of the input tensor
    input_shape = x.get_shape().as_list()

    # If the input shape is None, return the output shape
    if input_shape[0] is None:
        return output_shape

    # Otherwise, return the input shape with the reduced dimension replaced by 1
    return [input_shape[i] if i is not reduced_dim else 1 for i in range(len(input_shape))]