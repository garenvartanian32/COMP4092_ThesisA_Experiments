def boolean_difference(self, mesh, inplace=False):
        bfilter = vtk.vtkBooleanOperationPolyDataFilter()
        bfilter.SetOperationToDifference()
        bfilter.SetInputData(1, mesh)
        bfilter.SetInputData(0, self)
        bfilter.ReorientDifferenceCellsOff()
        bfilter.Update()
        mesh = _get_output(bfilter)
        if inplace:
            self.overwrite(mesh)
        else:
            return mesh