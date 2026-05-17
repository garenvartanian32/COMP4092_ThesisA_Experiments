def zap_disk(block_device):
    # https: 
    # sometimes sgdisk exits non-zero; this is OK, dd will clean up
    call(['sgdisk', '--zap-all', '--', block_device])
    call(['sgdisk', '--clear', '--mbrtogpt', '--', block_device])
    dev_end = check_output(['blockdev', '--getsz',
                            block_device]).decode('UTF-8')
    gpt_end = int(dev_end.split()[0]) - 100
    check_call(['dd', 'if=/dev/zero', 'of=%s' % (block_device),
                'bs=1M', 'count=1'])
    check_call(['dd', 'if=/dev/zero', 'of=%s' % (block_device),
                'bs=512', 'count=100', 'seek=%s' % (gpt_end)])