def _reduction_output_shape(x, output_shape, reduced_dim):
  if output_shape is None:
    if reduced_dim is None:
      return Shape([])
    else:
      if reduced_dim not in x.shape.dims:
        raise ValueError(
            "reduced_dim=%s not in x.shape.dims=%s" % (reduced_dim, x.shape))
      return x.shape - reduced_dim
  if reduced_dim is not None:
    if [reduced_dim] != [d for d in x.shape.dims if d not in output_shape.dims]:
      raise ValueError(
          "reduced_dim contradicts output_shape:"
          "x=%s output_shape=%s reduced_dim=%s" %
          (x, output_shape, reduced_dim))
  return output_shape