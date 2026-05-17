def checkpoint(self, eager=True):
        """Returns a checkpointed version of this Dataset. Checkpointing can be used to truncate the
        logical plan of this DataFrame, which is especially useful in iterative algorithms where the
        plan may grow exponentially. It will be saved to files inside the checkpoint
        directory set with L{SparkContext.setCheckpointDir()}.

        :param eager: Whether to checkpoint this DataFrame immediately

        .. note:: Experimental
        """
        jdf = self._jdf.checkpoint(eager)
        return DataFrame(jdf, self.sql_ctx)