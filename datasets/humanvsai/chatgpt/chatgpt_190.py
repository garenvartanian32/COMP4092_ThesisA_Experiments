def remove_common_prefix_suffix(files):
    # Finding the common prefix and suffix
    common_prefix = os.path.commonprefix(files)
    common_suffix = os.path.commonprefix(files[::-1])[::-1]

    # Removing the common prefix and suffix
    result = [f[len(common_prefix):-len(common_suffix)] for f in files]

    return result
