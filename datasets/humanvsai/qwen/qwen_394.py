def _convert_vpathlist(input_obj):
    if isinstance(input_obj, (list, tuple)):
        vpath_list = pgmagick.VPathList()
        for item in input_obj:
            if isinstance(item, pgmagick.VPath):
                vpath_list.append(item)
            else:
                raise TypeError('All items in the input object must be of type pgmagick.VPath')
        return vpath_list
    else:
        raise TypeError('Input object must be a list or tuple')