def get_stores():
    ret = dict()
    cmd = r"Get-ChildItem -Path 'Cert:\' | " \
          r"Select-Object LocationName, StoreNames"
    items = _cmd_run(cmd=cmd, as_json=True)
    for item in items:
        ret[item['LocationName']] = list()
        for store in item['StoreNames']:
            ret[item['LocationName']].append(store)
    return ret