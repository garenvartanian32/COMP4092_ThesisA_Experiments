def _jtime(self, timestamp):
        """ Convert datetime or unix_timestamp into Time
        """
        if isinstance(timestamp, datetime):
            timestamp = time.mktime(timestamp.timetuple())
        return self._sc._jvm.Time(long(timestamp * 1000))