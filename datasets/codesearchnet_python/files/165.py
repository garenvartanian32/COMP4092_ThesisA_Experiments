def getTaskInfos(self):
        """
        .. note:: Experimental

        Returns :class:`BarrierTaskInfo` for all tasks in this barrier stage,
        ordered by partition ID.

        .. versionadded:: 2.4.0
        """
        if self._port is None or self._secret is None:
            raise Exception("Not supported to call getTaskInfos() before initialize " +
                            "BarrierTaskContext.")
        else:
            addresses = self._localProperties.get("addresses", "")
            return [BarrierTaskInfo(h.strip()) for h in addresses.split(",")]