def do_lzop_put(creds, url, local_path, gpg_key):
    assert url.endswith('.lzo')
    blobstore = get_blobstore(storage.StorageLayout(url))
    with tempfile.NamedTemporaryFile(
            mode='r+b', buffering=pipebuf.PIPE_BUF_BYTES) as tf:
        with pipeline.get_upload_pipeline(
                open(local_path, 'rb'), tf, gpg_key=gpg_key):
            pass
        tf.flush()
        clock_start = time.time()
        tf.seek(0)
        k = blobstore.uri_put_file(creds, url, tf)
        clock_finish = time.time()
        kib_per_second = format_kib_per_second(
            clock_start, clock_finish, k.size)
        return kib_per_second