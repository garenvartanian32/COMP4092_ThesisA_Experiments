def get_files_from_filestore(job, files, work_dir, cache=True, docker=False):
    import os
    import tarfile
    import subprocess
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
    for (file_name, file_id) in files.items():
        file_path = job.fileStore.readGlobalFile(file_id, userPath=os.path.join(work_dir, file_name))
        if file_path.endswith('.tar.gz'):
            with tarfile.open(file_path, 'r:gz') as tar:
                tar.extractall(path=work_dir)
            os.remove(file_path)
            file_path = os.path.join(work_dir, os.path.splitext(os.path.splitext(file_name)[0])[0])
        if docker:
            file_path = os.path.join('/data', os.path.basename(file_path))
        print(f'File path for {file_name}: {file_path}')
    return file_path