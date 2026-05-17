def trainOn(self, dstream):
        """Train the model on the incoming dstream."""
        self._validate(dstream)

        def update(rdd):
            self._model.update(rdd, self._decayFactor, self._timeUnit)

        dstream.foreachRDD(update)