def slicenet_middle(inputs_encoded, targets, target_space_emb, mask, hparams):
  def norm_fn(x, name):
    with tf.variable_scope(name, default_name="norm"):
      return common_layers.apply_norm(x, hparams.norm_type, hparams.hidden_size,
                                      hparams.norm_epsilon)
  # Flatten targets and embed target_space_id.
  targets_flat = tf.expand_dims(common_layers.flatten4d3d(targets), axis=2)
  target_space_emb = tf.tile(target_space_emb,
                             [tf.shape(targets_flat)[0], 1, 1, 1])
  # Use attention from each target to look at input and retrieve.
  targets_shifted = common_layers.shift_right(
      targets_flat, pad_value=target_space_emb)
  if hparams.attention_type == "none":
    targets_with_attention = tf.zeros_like(targets_shifted)
  else:
    inputs_padding_bias = (1.0 - mask) * -1e9  # Bias to not attend to padding.
    targets_with_attention = attention(
        targets_shifted,
        inputs_encoded,
        norm_fn,
        hparams,
        bias=inputs_padding_bias)
  # Positional targets: merge attention and raw.
  kernel = (hparams.kernel_height, hparams.kernel_width)
  targets_merged = common_layers.subseparable_conv_block(
      tf.concat([targets_with_attention, targets_shifted], axis=3),
      hparams.hidden_size, [((1, 1), kernel)],
      normalizer_fn=norm_fn,
      padding="LEFT",
      separability=4,
      name="targets_merge")
  return targets_merged, 0.0