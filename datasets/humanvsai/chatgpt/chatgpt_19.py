def get_es_index(data_source, index=None):
    if index:
        return index
    if data_source == 'abc':
        return 'abc_index'
    elif data_source == 'xyz':
        return 'xyz_index'
    else:
        return 'default_index'
