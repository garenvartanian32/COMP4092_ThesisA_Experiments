import pgmagick

def convert_to_VPathList(input_obj):
    if not isinstance(input_obj, (list, tuple)):
        raise TypeError("Input object must be list or tuple.")
    path_list = pgmagick.VPathList()
    for path in input_obj:
        if not isinstance(path, (list, tuple)):
            raise TypeError("Paths must be lists or tuples.")
        vpath = pgmagick.VPath()
        for point in path:
            if not isinstance(point, (list, tuple)):
                raise TypeError("Path points must be lists or tuples.")
            vpath.push_back(pgmagick.LineToPathElement(point[0], point[1]))
        path_list.append(vpath)
    return path_list
