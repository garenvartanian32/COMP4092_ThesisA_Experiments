def _sort_cols(self, cols, kwargs):
        """ Return a JVM Seq of Columns that describes the sort order
        """
        if not cols:
            raise ValueError("should sort by at least one column")
        if len(cols) == 1 and isinstance(cols[0], list):
            cols = cols[0]
        jcols = [_to_java_column(c) for c in cols]
        ascending = kwargs.get('ascending', True)
        if isinstance(ascending, (bool, int)):
            if not ascending:
                jcols = [jc.desc() for jc in jcols]
        elif isinstance(ascending, list):
            jcols = [jc if asc else jc.desc()
                     for asc, jc in zip(ascending, jcols)]
        else:
            raise TypeError("ascending can only be boolean or list, but got %s" % type(ascending))
        return self._jseq(jcols)