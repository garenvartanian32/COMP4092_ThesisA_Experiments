def delete_principal(name):
    ret = {}
    cmd = __execute_kadmin('delprinc -force {0}'.format(name))
    if cmd['retcode'] != 0 or cmd['stderr']:
        ret['comment'] = cmd['stderr'].splitlines()[-1]
        ret['result'] = False
        return ret
    return True