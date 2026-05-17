def _convert_vpathlist(input_obj):
    vpl = pgmagick.VPathList()
    for obj in input_obj:
        # FIXME
        obj = pgmagick.PathMovetoAbs(pgmagick.Coordinate(obj[0], obj[1]))
        vpl.append(obj)
    return vpl