import tensorflow as tf

def convolution_operation(inputs, w):
    outputs = tf.nn.conv2d(inputs, w, strides=[1, 1, 1, 1], padding='SAME')
    return outputs
