def _reduction_output_shape(x, output_shape, reduced_dim):
    if not isinstance(output_shape, (tuple, list)):
        raise ValueError('output_shape must be a tuple or a list')
    if not isinstance(reduced_dim, (tuple, list)):
        raise ValueError('reduced_dim must be a tuple or a list')
    if len(output_shape) != x.ndim:
        raise ValueError('output_shape must have the same number of dimensions as x')
    if any((d < 0 or d >= x.ndim for d in reduced_dim)):
        raise ValueError('reduced_dim must contain valid dimensions')
    for i in range(x.ndim):
        if i not in reduced_dim and output_shape[i] != x.shape[i]:
            raise ValueError('output_shape must match the input shape except for the reduced dimensions')
    new_shape = list(x.shape)
    for d in reduced_dim:
        new_shape[d] = 1
    x_reshaped = x.reshape(new_shape)
    result = x_reshaped.sum(axis=reduced_dim)
    result = result.reshape(output_shape)
    return result