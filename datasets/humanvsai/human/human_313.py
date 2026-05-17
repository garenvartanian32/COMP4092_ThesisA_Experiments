def add_external_library(library):
    for command in ['build', 'build_ext', 'install']:
        add_command_option(command, str('use-system-' + library),
                           'Use the system {0} library'.format(library),
                           is_bool=True)