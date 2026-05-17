import vtki

def boolean_difference(self, mesh, inplace=False):
    """Combines two meshes and retains only the volume in common
    between the meshes.

    Parameters
    ----------
    mesh : vtki.PolyData
        The mesh to perform a union against.

    inplace : bool, optional
        Updates mesh in-place while returning nothing.

    Returns
    -------
    union : vtki.PolyData
        The union mesh when inplace=False.
    """
    # Create a boolean array to select the cells to keep
    selection = self.select_enclosed_points(mesh)

    # Create a new mesh with the selected cells
    difference = self.extract_geometry().threshold(selection)

    if inplace:
        self.copy_from_mesh(difference)
    else:
        return difference