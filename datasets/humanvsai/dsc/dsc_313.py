def add_external_library(library):
    """Add a build option for selecting the internal or system copy of a library.

    Parameters
    ----------
    library : str
        The name of the library.  If the library is `foo`, the build
        option will be called `--use-system-foo`.
    """
    # Create the build option
    build_option = "--use-system-" + library

    # Add the build option to the build options list
    # This will depend on how your build options are stored
    # For example, if you have a list called build_options:
    build_options.append(build_option)

    # Return the build option
    return build_option