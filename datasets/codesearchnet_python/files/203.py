def checkpoint(self, interval):
        """
        Enable periodic checkpointing of RDDs of this DStream

        @param interval: time in seconds, after each period of that, generated
                         RDD will be checkpointed
        """
        self.is_checkpointed = True
        self._jdstream.checkpoint(self._ssc._jduration(interval))
        return self