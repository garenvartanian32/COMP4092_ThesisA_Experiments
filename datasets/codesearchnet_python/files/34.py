def _get_local_dirs(sub):
    """ Get all the directories """
    path = os.environ.get("SPARK_LOCAL_DIRS", "/tmp")
    dirs = path.split(",")
    if len(dirs) > 1:
        # different order in different processes and instances
        rnd = random.Random(os.getpid() + id(dirs))
        random.shuffle(dirs, rnd.random)
    return [os.path.join(d, "python", str(os.getpid()), sub) for d in dirs]