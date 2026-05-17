def convert_softmax_layer(keras_layer, builder):
    from keras.layers import Softmax
    assert isinstance(keras_layer, Softmax), "The provided keras layer is not an instance of Softmax layer."
    assert keras_layer.get_config()['name'], "The provided keras layer has no name."
    coreml_layer = builder.add_softmax(name=keras_layer.get_config()['name'], input_name=keras_layer.input.name, output_name=keras_layer.output.name)
    return coreml_layer
