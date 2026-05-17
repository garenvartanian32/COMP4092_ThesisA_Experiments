def slicenet_middle(inputs_encoded, targets, target_space_emb, mask, hparams):
    inputs_encoded = inputs_encoded[:, :, :hparams['num_channels']]
    inputs_encoded = inputs_encoded * mask
    inputs_encoded = tf.concat([inputs_encoded, target_space_emb], axis=-1)
    inputs_encoded = tf.layers.dense(inputs_encoded, hparams['hidden_size'], activation=tf.nn.relu)
    inputs_encoded = tf.layers.dense(inputs_encoded, hparams['hidden_size'], activation=tf.nn.relu)
    inputs_encoded = tf.layers.dropout(inputs_encoded, rate=hparams['dropout_rate'], training=hparams['is_training'])
    inputs_encoded = tf.layers.dense(inputs_encoded, hparams['num_channels'], activation=None)
    outputs = inputs_encoded + targets
    return outputs