def velocity(msg):
    if 5 <= typecode(msg) <= 8:
        return surface_velocity(msg)
    elif typecode(msg) == 19:
        return airborne_velocity(msg)
    else:
        raise RuntimeError("incorrect or inconsistant message types, expecting 4<TC<9 or TC=19")