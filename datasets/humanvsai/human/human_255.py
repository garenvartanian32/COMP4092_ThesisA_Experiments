def add_arguments(self, parser):
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-l', '--list', nargs='?',
                           type=str.lower, default='_',
                           choices=['usb', 'ip'],
                           help='list all the connected emulators')
        group.add_argument('-s', '--supported', nargs=1,
                           help='query whether a device is supported')
        group.add_argument('-t', '--test', action='store_true',
                           help='perform a self-test')
        return None