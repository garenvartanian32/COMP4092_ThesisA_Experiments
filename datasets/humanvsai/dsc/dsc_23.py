import argparse

def add_arguments(argument_group):
    """Adds command line arguments to an argument group.

    This function takes an argument group and adds
    to it all the command line arguments this helper supports.

    Args:
      argument_group (argparse._ArgumentGroup):
          argparse group.
    """
    # Add an argument
    argument_group.add_argument("--argument_name", help="help message for the argument")

# Create the parser
parser = argparse.ArgumentParser()

# Create the group
group = parser.add_argument_group('group_name')

# Add arguments to the group
add_arguments(group)

# Parse the arguments
args = parser.parse_args()