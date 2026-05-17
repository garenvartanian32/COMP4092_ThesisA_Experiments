def over(self, window):
        """
        Define a windowing column.

        :param window: a :class:`WindowSpec`
        :return: a Column

        >>> from pyspark.sql import Window
        >>> window = Window.partitionBy("name").orderBy("age").rowsBetween(-1, 1)
        >>> from pyspark.sql.functions import rank, min
        >>> # df.select(rank().over(window), min('age').over(window))
        """
        from pyspark.sql.window import WindowSpec
        if not isinstance(window, WindowSpec):
            raise TypeError("window should be WindowSpec")
        jc = self._jc.over(window._jspec)
        return Column(jc)