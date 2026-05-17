def vertex_defects(mesh):
    angle_sum = np.asarray(mesh.face_angles_sparse.sum(axis=1)).flatten()
    defect = (2 * np.pi) - angle_sum
    return defect