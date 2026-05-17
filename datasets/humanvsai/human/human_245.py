def generate_catalogue_subparser(subparsers):
    parser = subparsers.add_parser(
        'catalogue', description=constants.CATALOGUE_DESCRIPTION,
        epilog=constants.CATALOGUE_EPILOG,
        formatter_class=ParagraphFormatter, help=constants.CATALOGUE_HELP)
    utils.add_common_arguments(parser)
    parser.set_defaults(func=generate_catalogue)
    parser.add_argument('corpus', help=constants.DB_CORPUS_HELP,
                        metavar='CORPUS')
    utils.add_query_arguments(parser)
    parser.add_argument('-l', '--label', default='',
                        help=constants.CATALOGUE_LABEL_HELP)