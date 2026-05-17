def continuous_decode_on_eval_data(self):
    if self._hparams.mlperf_mode:
      ckpt_generator = next_undecoded_checkpoint(
          self._hparams.model_dir, self._decode_hparams.decode_timeout_mins)
    else:
      ckpt_generator = next_checkpoint(self._hparams.model_dir,
                                       self._decode_hparams.decode_timeout_mins)
    for ckpt in ckpt_generator:
      current_step = decoding.get_step_from_ckpt_path(ckpt)
      tf.logging.info("Decoding step %d" % current_step)
      # Skip checkpoint 0.
      if current_step == 0:
        continue
      # Decode the latest checkpoint by default.
      checkpoint_path = None
      if self._hparams.mlperf_mode:
        self._decode_hparams.mlperf_decode_step = current_step
        checkpoint_path = ckpt
      mlperf_log.transformer_print(key=mlperf_log.EVAL_START)
      self.decode(
          dataset_split=tf.estimator.ModeKeys.EVAL,
          checkpoint_path=checkpoint_path)
      d_hparams = self._decode_hparams
      if self._hparams.mlperf_mode and d_hparams.mlperf_success:
        mlperf_log.transformer_print(
            key=mlperf_log.RUN_STOP, value={"success": "true"})
        break
    d_hparams = self._decode_hparams
    if self._hparams.mlperf_mode and not d_hparams.mlperf_success:
      mlperf_log.transformer_print(
          key=mlperf_log.RUN_STOP, value={"success": "false"})