def hint(self, name, *parameters):
        """Specifies some hint on the current DataFrame.

        :param name: A name of the hint.
        :param parameters: Optional parameters.
        :return: :class:`DataFrame`

        >>> df.join(df2.hint("broadcast"), "name").show()
        +----+---+------+
        |name|age|height|
        +----+---+------+
        | Bob|  5|    85|
        +----+---+------+
        """
        if len(parameters) == 1 and isinstance(parameters[0], list):
            parameters = parameters[0]

        if not isinstance(name, str):
            raise TypeError("name should be provided as str, got {0}".format(type(name)))

        allowed_types = (basestring, list, float, int)
        for p in parameters:
            if not isinstance(p, allowed_types):
                raise TypeError(
                    "all parameters should be in {0}, got {1} of type {2}".format(
                        allowed_types, p, type(p)))

        jdf = self._jdf.hint(name, self._jseq(parameters))
        return DataFrame(jdf, self.sql_ctx)