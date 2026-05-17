def discretize_path(entities, vertices, path, scale=1.0):
    discrete = []
    for index in path:
        entity = entities[index]
        if isinstance(entity, Line):
            discrete.extend(entity.discretize(vertices, scale))
        elif isinstance(entity, Arc):
            discrete.extend(entity.discretize(vertices, scale))
        # Add more elif statements for other entity types
    return discrete