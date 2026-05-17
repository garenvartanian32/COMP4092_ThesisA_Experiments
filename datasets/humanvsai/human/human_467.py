def discretize_path(entities, vertices, path, scale=1.0):
    # make sure vertices are numpy array
    vertices = np.asanyarray(vertices)
    path_len = len(path)
    if path_len == 0:
        raise ValueError('Cannot discretize empty path!')
    if path_len == 1:
        # case where we only have one entity
        discrete = np.asanyarray(entities[path[0]].discrete(
            vertices,
            scale=scale))
    else:
        # run through path appending each entity
        discrete = []
        for i, entity_id in enumerate(path):
            # the current (n, dimension) discrete curve of an entity
            current = entities[entity_id].discrete(vertices, scale=scale)
            # check if we are on the final entity
            if i >= (path_len - 1):
                # if we are on the last entity include the last point
                discrete.append(current)
            else:
                # slice off the last point so we don't get duplicate
                # points from the end of one entity and the start of another
                discrete.append(current[:-1])
        # stack all curves to one nice (n, dimension) curve
        discrete = np.vstack(discrete)
    # make sure 2D curves are are counterclockwise
    if vertices.shape[1] == 2 and not is_ccw(discrete):
        # reversing will make array non c- contiguous
        discrete = np.ascontiguousarray(discrete[::-1])
    return discrete