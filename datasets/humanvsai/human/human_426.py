def pkg_config_libdirs(packages):
    # don't try calling pkg-config if NO_PKGCONFIG is set in environment
    if os.environ.get("NO_PKGCONFIG", None):
        return []
    # if calling pkg-config failes, don't continue and don't try again.
    try:
        FNULL = open(os.devnull, 'w')
        subprocess.check_call(["pkg-config", "--version"], stdout=FNULL, close_fds=True)
    except:
        print("PyCBC.libutils: pkg-config call failed, setting NO_PKGCONFIG=1",
              file=sys.stderr)
        os.environ['NO_PKGCONFIG'] = "1"
        return []
    # First, check that we can call pkg-config on each package in the list
    for pkg in packages:
        if not pkg_config_check_exists(pkg):
            raise ValueError("Package {0} cannot be found on the pkg-config search path".format(pkg))
    libdirs = []
    for token in getoutput("PKG_CONFIG_ALLOW_SYSTEM_LIBS=1 pkg-config --libs-only-L {0}".format(' '.join(packages))).split():
        if token.startswith("-L"):
            libdirs.append(token[2:])
    return libdirs