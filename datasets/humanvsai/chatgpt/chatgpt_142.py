def mesh_union(mesh, inplace=False):
    # imports
    import vtki
    import numpy as np
    
    # make a copy of the input mesh
    mesh_union = mesh.copy()
    
    # calculate the intersection between the two meshes
    intersection = mesh.boolean_intersection(mesh_union)
    
    # find cells in the intersection mesh
    cells_intersection = intersection.cell_arrays['CellIds']
    
    # find cells in the original mesh that intersect with intersection cells
    cells = np.zeros(mesh.n_cells, dtype=np.bool)
    cells[cells_intersection] = True
    cells &= mesh.cell_arrays['Visibility']
    
    # apply mask to original mesh
    mesh_union.cell_arrays['Visibility'][~cells] = 0
    
    if inplace:
        # update mesh in-place
        mesh = mesh_union
    else:
        # return union mesh
        return mesh_union
