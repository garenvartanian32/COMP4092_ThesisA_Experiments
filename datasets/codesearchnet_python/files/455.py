def U(self):
        """
        Returns a distributed matrix whose columns are the left
        singular vectors of the SingularValueDecomposition if computeU was set to be True.
        """
        u = self.call("U")
        if u is not None:
            mat_name = u.getClass().getSimpleName()
            if mat_name == "RowMatrix":
                return RowMatrix(u)
            elif mat_name == "IndexedRowMatrix":
                return IndexedRowMatrix(u)
            else:
                raise TypeError("Expected RowMatrix/IndexedRowMatrix got %s" % mat_name)