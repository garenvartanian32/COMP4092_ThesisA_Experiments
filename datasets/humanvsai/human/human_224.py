def write_ioc(root, output_dir=None, force=False):
    root_tag = 'OpenIOC'
    if not force and root.tag != root_tag:
        raise ValueError('Root tag is not "{}".'.format(root_tag))
    default_encoding = 'utf-8'
    tree = root.getroottree()
    # noinspection PyBroadException
    try:
        encoding = tree.docinfo.encoding
    except:
        log.debug('Failed to get encoding from docinfo')
        encoding = default_encoding
    ioc_id = root.attrib['id']
    fn = ioc_id + '.ioc'
    if output_dir:
        fn = os.path.join(output_dir, fn)
    else:
        fn = os.path.join(os.getcwd(), fn)
    try:
        with open(fn, 'wb') as fout:
            fout.write(et.tostring(tree, encoding=encoding, xml_declaration=True, pretty_print=True))
    except (IOError, OSError):
        log.exception('Failed to write out IOC')
        return False
    except:
        raise
    return True