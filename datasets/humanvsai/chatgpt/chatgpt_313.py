def add_build_option(library):
    """
    Add a build option for selecting the internal or system copy of a library.

    Parameters
    ----------
    library : str
        The name of the library.  If the library is `foo`, the build
        option will be called `--use-system-foo`.

    """
    option_name = '--use-system-' + library
    print(f"Added {option_name} to build options.")
    # Implement actual code to add build option here
