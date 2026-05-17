from pgmagick import VPathList

def _convert_vpathlist(input_obj):
    """convert from 'list' or 'tuple' object to pgmagick.VPathList.

    :type input_obj: list or tuple
    """
    if isinstance(input_obj, (list, tuple)):
        vpath_list = VPathList()
        for item in input_obj:
            vpath_list.push_back(item)
        return vpath_list
    else:
        raise TypeError("Input must be a list or tuple")