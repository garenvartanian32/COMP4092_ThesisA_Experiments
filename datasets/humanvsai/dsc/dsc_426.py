import pkg_resources

def pkg_config_libdirs(packages):
    libdirs = []
    for package in packages:
        try:
            metadata = pkg_resources.get_metadata(package)
            libdirs.append(metadata.get('library_dirs'))
        except pkg_resources.DistributionNotFound:
            continue
    return libdirs