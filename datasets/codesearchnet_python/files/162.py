def _getOrCreate(cls):
        """
        Internal function to get or create global BarrierTaskContext. We need to make sure
        BarrierTaskContext is returned from here because it is needed in python worker reuse
        scenario, see SPARK-25921 for more details.
        """
        if not isinstance(cls._taskContext, BarrierTaskContext):
            cls._taskContext = object.__new__(cls)
        return cls._taskContext