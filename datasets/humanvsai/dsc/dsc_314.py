import tensorflow as tf

def _apply_conv(self, inputs, w):
    # Ensure inputs and w are of the same type
    assert inputs.dtype == w.dtype

    # Ensure inputs and w are of the same shape
    assert inputs.shape == w.shape

    # Perform convolution
    outputs = tf.nn.conv2d(inputs, w, strides=[1, 1, 1, 1], padding='SAME')

    return outputs