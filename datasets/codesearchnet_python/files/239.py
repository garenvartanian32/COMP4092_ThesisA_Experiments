def withWatermark(self, eventTime, delayThreshold):
        """Defines an event time watermark for this :class:`DataFrame`. A watermark tracks a point
        in time before which we assume no more late data is going to arrive.

        Spark will use this watermark for several purposes:
          - To know when a given time window aggregation can be finalized and thus can be emitted
            when using output modes that do not allow updates.

          - To minimize the amount of state that we need to keep for on-going aggregations.

        The current watermark is computed by looking at the `MAX(eventTime)` seen across
        all of the partitions in the query minus a user specified `delayThreshold`.  Due to the cost
        of coordinating this value across partitions, the actual watermark used is only guaranteed
        to be at least `delayThreshold` behind the actual event time.  In some cases we may still
        process records that arrive more than `delayThreshold` late.

        :param eventTime: the name of the column that contains the event time of the row.
        :param delayThreshold: the minimum delay to wait to data to arrive late, relative to the
            latest record that has been processed in the form of an interval
            (e.g. "1 minute" or "5 hours").

        .. note:: Evolving

        >>> sdf.select('name', sdf.time.cast('timestamp')).withWatermark('time', '10 minutes')
        DataFrame[name: string, time: timestamp]
        """
        if not eventTime or type(eventTime) is not str:
            raise TypeError("eventTime should be provided as a string")
        if not delayThreshold or type(delayThreshold) is not str:
            raise TypeError("delayThreshold should be provided as a string interval")
        jdf = self._jdf.withWatermark(eventTime, delayThreshold)
        return DataFrame(jdf, self.sql_ctx)