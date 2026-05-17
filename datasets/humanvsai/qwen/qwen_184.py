def zipdir(src_path, target_path, wrapdir=''):
    import os
    import zipfile
    with zipfile.ZipFile(target_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for (root, dirs, files) in os.walk(src_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=src_path)
                if wrapdir:
                    arcname = os.path.join(wrapdir, arcname)
                zipf.write(file_path, arcname)