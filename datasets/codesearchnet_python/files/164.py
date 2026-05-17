def barrier(self):
        """
        .. note:: Experimental

        Sets a global barrier and waits until all tasks in this stage hit this barrier.
        Similar to `MPI_Barrier` function in MPI, this function blocks until all tasks
        in the same stage have reached this routine.

        .. warning:: In a barrier stage, each task much have the same number of `barrier()`
            calls, in all possible code branches.
            Otherwise, you may get the job hanging or a SparkException after timeout.

        .. versionadded:: 2.4.0
        """
        if self._port is None or self._secret is None:
            raise Exception("Not supported to call barrier() before initialize " +
                            "BarrierTaskContext.")
        else:
            _load_from_socket(self._port, self._secret)