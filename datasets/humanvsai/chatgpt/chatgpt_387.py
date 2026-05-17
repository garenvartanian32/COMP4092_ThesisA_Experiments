import numpy as np

def get_vertex_defect(vertices, faces):
    vertex_defect = np.zeros(len(vertices), dtype=float)
    for idx, vertex in enumerate(vertices):
        angles = []
        for face in faces:
            if idx in face:
                v0, v1, v2 = [vertices[vidx] for vidx in face if vidx != idx]
                vector1 = v0 - vertex
                vector2 = v1 - vertex
                vector3 = v2 - vertex
                angle1 = np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
                angle2 = np.arccos(np.dot(vector2, vector3) / (np.linalg.norm(vector2) * np.linalg.norm(vector3)))
                angle3 = np.arccos(np.dot(vector1, vector3) / (np.linalg.norm(vector1) * np.linalg.norm(vector3)))
                angles.append(angle1 + angle2 + angle3)
        if angles:
            vertex_defect[idx] = 2 * np.pi - sum(angles)
    return vertex_defect
