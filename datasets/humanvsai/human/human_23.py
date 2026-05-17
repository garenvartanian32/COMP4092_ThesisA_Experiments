def AddArguments(cls, argument_group):
    argument_group.add_argument(
        '--preferred_year', '--preferred-year', dest='preferred_year',
        type=int, action='store', default=None, metavar='YEAR', help=(
            'When a format\'s timestamp does not include a year, e.g. '
            'syslog, use this as the initial year instead of attempting '
            'auto-detection.'))
    argument_group.add_argument(
        '--process_archives', '--process-archives', dest='process_archives',
        action='store_true', default=False, help=(
            'Process file entries embedded within archive files, such as '
            'archive.tar and archive.zip. This can make processing '
            'significantly slower.'))
    argument_group.add_argument(
        '--skip_compressed_streams', '--skip-compressed-streams',
        dest='process_compressed_streams', action='store_false', default=True,
        help=(
            'Skip processing file content within compressed streams, such as '
            'syslog.gz and syslog.bz2.'))