def getCheckpointFile(self):
        """
        Gets the name of the file to which this RDD was checkpointed

        Not defined if RDD is checkpointed locally.
        """
        checkpointFile = self._jrdd.rdd().getCheckpointFile()
        if checkpointFile.isDefined():
            return checkpointFile.get()