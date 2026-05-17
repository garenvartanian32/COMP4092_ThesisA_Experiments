def _apply_conv(self, inputs, w):
    import tensorflow as tf
    outputs = tf.nn.conv2d(inputs, w, strides=[1, 1, 1, 1], padding='SAME', data_format='NHWC')
    return outputs