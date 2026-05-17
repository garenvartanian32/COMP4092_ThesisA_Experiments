def add_arguments(self, parser):
    # Add arguments to the parser
    parser.add_argument('arg1', type=str, help='Description of argument 1')
    parser.add_argument('arg2', type=int, help='Description of argument 2')
    parser.add_argument('-opt', type=bool, help='Description of optional argument')
    # or parser.add_argument('-opt', action='store_true', help='Description of optional argument')
    return None
