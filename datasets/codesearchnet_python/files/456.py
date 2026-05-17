def rows(self):
        """
        Rows of the IndexedRowMatrix stored as an RDD of IndexedRows.

        >>> mat = IndexedRowMatrix(sc.parallelize([IndexedRow(0, [1, 2, 3]),
        ...                                        IndexedRow(1, [4, 5, 6])]))
        >>> rows = mat.rows
        >>> rows.first()
        IndexedRow(0, [1.0,2.0,3.0])
        """
        # We use DataFrames for serialization of IndexedRows from
        # Java, so we first convert the RDD of rows to a DataFrame
        # on the Scala/Java side. Then we map each Row in the
        # DataFrame back to an IndexedRow on this side.
        rows_df = callMLlibFunc("getIndexedRows", self._java_matrix_wrapper._java_model)
        rows = rows_df.rdd.map(lambda row: IndexedRow(row[0], row[1]))
        return rows