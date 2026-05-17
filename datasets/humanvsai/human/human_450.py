def read_checksum_digest(path, checksum_cls=hashlib.sha256):
  checksum = checksum_cls()
  size = 0
  with tf.io.gfile.GFile(path, "rb") as f:
    while True:
      block = f.read(io.DEFAULT_BUFFER_SIZE)
      size += len(block)
      if not block:
        break
      checksum.update(block)
  return checksum.hexdigest(), size