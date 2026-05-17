def _jseq(self, cols, converter=None):
        """Return a JVM Seq of Columns from a list of Column or names"""
        return _to_seq(self.sql_ctx._sc, cols, converter)