def _apply_conv(self, inputs, w):
    outputs = tf.nn.convolution(inputs, w, strides=self._stride,
                                padding=self._conv_op_padding,
                                dilation_rate=self._rate,
                                data_format=self._data_format)
    return outputs