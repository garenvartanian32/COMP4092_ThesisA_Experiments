def save_file(f, full_path):
    make_dirs_for_file_path(full_path, mode=dju_settings.DJU_IMG_CHMOD_DIR)
    with open(full_path, 'wb') as t:
        f.seek(0)
        while True:
            buf = f.read(dju_settings.DJU_IMG_RW_FILE_BUFFER_SIZE)
            if not buf:
                break
            t.write(buf)
    os.chmod(full_path, dju_settings.DJU_IMG_CHMOD_FILE)