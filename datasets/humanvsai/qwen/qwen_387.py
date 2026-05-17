def vertex_defects(mesh):
    vertex_defects = np.zeros(len(mesh.vertices))
    for face in mesh.faces:
        (v1, v2, v3) = mesh.vertices[face]
        edge1 = v2 - v1
        edge2 = v3 - v1
        edge3 = v3 - v2
        angle1 = np.arccos(np.dot(edge1, edge2) / (np.linalg.norm(edge1) * np.linalg.norm(edge2)))
        angle2 = np.arccos(np.dot(edge2, edge3) / (np.linalg.norm(edge2) * np.linalg.norm(edge3)))
        angle3 = np.arccos(np.dot(edge3, edge1) / (np.linalg.norm(edge3) * np.linalg.norm(edge1)))
        face_angle_sum = angle1 + angle2 + angle3
        for vertex in face:
            vertex_defects[vertex] += 2 * np.pi - face_angle_sum
    for vertex in range(len(mesh.vertices)):
        num_faces = len([face for face in mesh.faces if vertex in face])
        if num_faces > 0:
            vertex_defects[vertex] /= num_faces
    return vertex_defects