def _convert_labeled_point_to_libsvm(p):
        """Converts a LabeledPoint to a string in LIBSVM format."""
        from pyspark.mllib.regression import LabeledPoint
        assert isinstance(p, LabeledPoint)
        items = [str(p.label)]
        v = _convert_to_vector(p.features)
        if isinstance(v, SparseVector):
            nnz = len(v.indices)
            for i in xrange(nnz):
                items.append(str(v.indices[i] + 1) + ":" + str(v.values[i]))
        else:
            for i in xrange(len(v)):
                items.append(str(i + 1) + ":" + str(v[i]))
        return " ".join(items)