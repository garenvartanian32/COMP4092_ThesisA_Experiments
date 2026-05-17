def get_files_from_filestore(job, files, work_dir, cache=True, docker=False):
    for name in files.keys():
        outfile = job.fileStore.readGlobalFile(files[name], '/'.join([work_dir, name]), cache=cache)
        # If the file pointed to a tarball, extract it to WORK_DIR
        if tarfile.is_tarfile(outfile) and file_xext(outfile).startswith('.tar'):
            untar_name = os.path.basename(strip_xext(outfile))
            files[untar_name] = untargz(outfile, work_dir)
            files.pop(name)
            name = os.path.basename(untar_name)
        # If the file is gzipped but NOT a tarfile, gunzip it to work_dir. However, the file is
        # already named x.gz so we need to write to a temporary file x.gz_temp then do a move
        # operation to overwrite x.gz.
        elif is_gzipfile(outfile) and file_xext(outfile) == '.gz':
            ungz_name = strip_xext(outfile)
            with gzip.open(outfile, 'rb') as gz_in, open(ungz_name, 'w') as ungz_out:
                shutil.copyfileobj(gz_in, ungz_out)
            files[os.path.basename(ungz_name)] = outfile
            files.pop(name)
            name = os.path.basename(ungz_name)
        else:
            files[name] = outfile
        # If the files will be sent to docker, we will mount work_dir to the container as /data and
        # we want the /data prefixed path to the file
        if docker:
            files[name] = docker_path(files[name])
    return files