def add_catalogue_parser(subparsers):
    catalogue_parser = subparsers.add_parser('catalogue', help='Generate and save catalogue')
    catalogue_parser.add_argument('output_file', help='Path to save catalogue file')
