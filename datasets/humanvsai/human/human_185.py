def patch_spyder3(verbose=False):
    try:
        # patch spyder/config/utils.py for file extension
        from spyder.config import utils
        src_file = utils.__file__
        spyder_dir = os.path.dirname(os.path.dirname(src_file))
        patch_file(src_file,
        '''
    (_("Cython/Pyrex files"), ('.pyx', '.pxd', '.pxi')),
    (_("C files"), ('.c', '.h')),''',
        '''
    (_("Cython/Pyrex files"), ('.pyx', '.pxd', '.pxi')),
    (_("SoS files"), ('.sos', )),
    (_("C files"), ('.c', '.h')),''',
            verbose=verbose)
        #
        # patch spyder/app/cli_options.py to add command line option --kernel
        patch_file(os.path.join(spyder_dir, 'app', 'cli_options.py'),
            '''help="String to show in the main window title")
    options, args = parser.parse_args()''',
            '''help="String to show in the main window title")
    parser.add_option('--kernel', help="Jupyter kernel to start.")
    options, args = parser.parse_args()''',
            verbose=verbose)
        #
        # patch spyder/utils/sourcecode.py,
        patch_file(os.path.join(spyder_dir, 'utils', 'sourcecode.py'),
                "'Python': ('py', 'pyw', 'python', 'ipy')",
                "'Python': ('py', 'pyw', 'python', 'ipy', 'sos')",
            verbose=verbose)
        patch_file(os.path.join(spyder_dir, 'utils', 'sourcecode.py'),
                '''CELL_LANGUAGES = {'Python': ('#%%', '# %%', '# <codecell>', '# In[')}''',
                '''CELL_LANGUAGES = {'Python': ('#%%', '# %%', '# <codecell>', '# In[', '%cell')}''',
            verbose=verbose)
        #
        # patch spyder/app/mainwindow.py
        patch_file(os.path.join(spyder_dir, 'app', 'mainwindow.py'),
            '''
    app.exec_()
''',
            r'''
    try:
        if options.kernel == 'sos':
            cfg_file = os.path.expanduser('~/.ipython/profile_default/ipython_config.py')
            has_cfg = os.path.isfile(cfg_file)
            if has_cfg and not os.path.isfile(cfg_file + '.sos_bak'):
                os.rename(cfg_file, cfg_file + '.sos_bak')
            with open(cfg_file, 'w') as cfg:
                cfg.write("c.IPKernelApp.kernel_class =  'sos_notebook.spyder_kernel.SoS_SpyderKernel'\n")
        app.exec_()
    finally:
        if options.kernel == 'sos':
            os.remove(cfg_file)
            if os.path.isfile(cfg_file + '.sos_bak'):
                os.rename(cfg_file + '.sos_bak', cfg_file)
''',
            verbose=verbose)
        #
        print('\nSpyder is successfully patched to accept .sos format and sos kernel.')
        print('Use ')
        print()
        print('    $ spyder --kernel sos')
        print()
        print('to start spyder with sos kernel')
    except Exception as e:
        sys.exit('Failed to patch spyder: {}'.format(e))