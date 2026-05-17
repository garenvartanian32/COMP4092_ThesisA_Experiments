def _initialize(cls, port, secret):
        """
        Initialize BarrierTaskContext, other methods within BarrierTaskContext can only be called
        after BarrierTaskContext is initialized.
        """
        cls._port = port
        cls._secret = secret