import argparse

def generate_catalogue_subparser(subparsers):
    """Adds a sub-command parser to `subparsers` to generate and save
    a catalogue file."""
    # create the parser for the "generate" command
    parser_generate = subparsers.add_parser('generate')

    # add arguments
    parser_generate.add_argument('-o', '--output', required=True, help='Output file')
    parser_generate.add_argument('-c', '--catalogue', required=True, help='Catalogue file')

    # set the function to be called when this sub-command is used
    parser_generate.set_defaults(func=generate_catalogue)

def generate_catalogue(args):
    """Generate and save a catalogue file."""
    # TODO: implement this function
    pass