def localCheckpoint(self, eager=True):
        """Returns a locally checkpointed version of this Dataset. Checkpointing can be used to
        truncate the logical plan of this DataFrame, which is especially useful in iterative
        algorithms where the plan may grow exponentially. Local checkpoints are stored in the
        executors using the caching subsystem and therefore they are not reliable.

        :param eager: Whether to checkpoint this DataFrame immediately

        .. note:: Experimental
        """
        jdf = self._jdf.localCheckpoint(eager)
        return DataFrame(jdf, self.sql_ctx)