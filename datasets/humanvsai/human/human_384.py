def convert_permute(builder, layer, input_names, output_names, keras_layer):
    input_name, output_name = (input_names[0], output_names[0])
    keras_dims = keras_layer.dims
    # Keras permute layer index begins at 1
    if len(keras_dims) == 3:
        # Keras input tensor interpret as (H,W,C)
        x = list(_np.array(keras_dims))
        arr = [2, 3, 1]  # HWC in Keras
        arr_permuted = [arr[x[0] - 1], arr[x[1] - 1], arr[x[2] - 1]]
        arr_permuted = [arr_permuted[2], arr_permuted[0], arr_permuted[1]]  # coreml format: channel first
        # add a sequence axis
        dim = [0] + arr_permuted
        dim = tuple(dim)
    elif len(keras_dims) == 4:
        # Here we use Keras converter as a place holder for inserting
        # permutations - the values here are not valid Keras dim parameters
        # but parameters we need to use to convert to CoreML model
        dim = keras_dims
    else:
        raise NotImplementedError('Supports only 3d permutation.')
    builder.add_permute(name = layer, dim=dim, input_name = input_name,
            output_name = output_name)