def discretize_path(entities, vertices, path, scale=1.0):
    import numpy as np
    discrete = []
    for (i, entity_index) in enumerate(path):
        entity = entities[entity_index]
        if i == 0:
            start_vertex = vertices[entity.start]
            discrete.append(start_vertex)
        if i == len(path) - 1:
            end_vertex = vertices[entity.end]
            discrete.append(end_vertex)
        if hasattr(entity, 'intermediate_points'):
            intermediate_points = entity.intermediate_points(vertices, scale)
            discrete.extend(intermediate_points)
    return np.array(discrete)