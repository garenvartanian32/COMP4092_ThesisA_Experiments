def convert_permute(builder, layer, input_names, output_names, keras_layer):
    if isinstance(keras_layer, keras.layers.Softmax):
        axis = keras_layer.axis
        builder.add_softmax(name=layer, input_name=input_names[0], output_name=output_names[0], axis=axis)
    else:
        raise ValueError('The layer is not a softmax layer')