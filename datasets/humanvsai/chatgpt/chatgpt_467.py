def get_path_points(entities, vertices, path, scale):
    points = []
    for index in path:
        entity = entities[index]
        if entity.type == 'Line':
            start, end = entity.start, entity.end
            points.extend([vertices[start], vertices[end]])
        elif entity.type == 'Arc':
            arc_points = get_arc_points(entity, vertices, scale)
            points.extend(arc_points)
    # Connect the points in the path
    discrete = []
    for i in range(len(points) - 1):
        start, end = points[i], points[i+1]
        segment = get_line_segment(start, end, scale)
        discrete.extend(segment)
    return np.array(discrete)
    
def get_arc_points(arc_entity, vertices, scale, num_points=20):
    center = vertices[arc_entity.center]
    radius = arc_entity.radius
    start, end = arc_entity.start, arc_entity.end
    sweep = arc_entity.sweep
    arc_points = []
    for i in range(num_points + 1):
        angle = start + i / num_points * sweep
        point = center + radius * np.array([math.cos(angle), math.sin(angle)])
        arc_points.append(point)
    return arc_points

def get_line_segment(start, end, scale, num_points=5):
    segment = []
    direction = end - start
    magnitude = np.linalg.norm(direction)
    if magnitude == 0:
        return [start]
    for i in range(num_points + 1):
        point = start + i / num_points * direction
        segment.append(point)
    return segment
