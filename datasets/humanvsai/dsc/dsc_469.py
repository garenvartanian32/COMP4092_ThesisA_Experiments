import os

def resolve_variables(self, provided_variables):
    """Resolve the values of the blueprint variables.

    This will resolve the values of the `VARIABLES` with values from the
    env file, the config, and any lookups resolved.

    Args:
        provided_variables (list of :class:`stacker.variables.Variable`):
            list of provided variables
    """
    # Assuming that provided_variables is a list of strings
    # and you want to replace them with their corresponding environment variable
    for i, var in enumerate(provided_variables):
        if var in os.environ:
            provided_variables[i] = os.environ[var]