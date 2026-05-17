def toPandas(self):
        """
        Returns the contents of this :class:`DataFrame` as Pandas ``pandas.DataFrame``.

        This is only available if Pandas is installed and available.

        .. note:: This method should only be used if the resulting Pandas's DataFrame is expected
            to be small, as all the data is loaded into the driver's memory.

        .. note:: Usage with spark.sql.execution.arrow.enabled=True is experimental.

        >>> df.toPandas()  # doctest: +SKIP
           age   name
        0    2  Alice
        1    5    Bob
        """
        from pyspark.sql.utils import require_minimum_pandas_version
        require_minimum_pandas_version()

        import pandas as pd

        if self.sql_ctx._conf.pandasRespectSessionTimeZone():
            timezone = self.sql_ctx._conf.sessionLocalTimeZone()
        else:
            timezone = None

        if self.sql_ctx._conf.arrowEnabled():
            use_arrow = True
            try:
                from pyspark.sql.types import to_arrow_schema
                from pyspark.sql.utils import require_minimum_pyarrow_version

                require_minimum_pyarrow_version()
                to_arrow_schema(self.schema)
            except Exception as e:

                if self.sql_ctx._conf.arrowFallbackEnabled():
                    msg = (
                        "toPandas attempted Arrow optimization because "
                        "'spark.sql.execution.arrow.enabled' is set to true; however, "
                        "failed by the reason below:\n  %s\n"
                        "Attempting non-optimization as "
                        "'spark.sql.execution.arrow.fallback.enabled' is set to "
                        "true." % _exception_message(e))
                    warnings.warn(msg)
                    use_arrow = False
                else:
                    msg = (
                        "toPandas attempted Arrow optimization because "
                        "'spark.sql.execution.arrow.enabled' is set to true, but has reached "
                        "the error below and will not continue because automatic fallback "
                        "with 'spark.sql.execution.arrow.fallback.enabled' has been set to "
                        "false.\n  %s" % _exception_message(e))
                    warnings.warn(msg)
                    raise

            # Try to use Arrow optimization when the schema is supported and the required version
            # of PyArrow is found, if 'spark.sql.execution.arrow.enabled' is enabled.
            if use_arrow:
                try:
                    from pyspark.sql.types import _check_dataframe_localize_timestamps
                    import pyarrow
                    batches = self._collectAsArrow()
                    if len(batches) > 0:
                        table = pyarrow.Table.from_batches(batches)
                        # Pandas DataFrame created from PyArrow uses datetime64[ns] for date type
                        # values, but we should use datetime.date to match the behavior with when
                        # Arrow optimization is disabled.
                        pdf = table.to_pandas(date_as_object=True)
                        return _check_dataframe_localize_timestamps(pdf, timezone)
                    else:
                        return pd.DataFrame.from_records([], columns=self.columns)
                except Exception as e:
                    # We might have to allow fallback here as well but multiple Spark jobs can
                    # be executed. So, simply fail in this case for now.
                    msg = (
                        "toPandas attempted Arrow optimization because "
                        "'spark.sql.execution.arrow.enabled' is set to true, but has reached "
                        "the error below and can not continue. Note that "
                        "'spark.sql.execution.arrow.fallback.enabled' does not have an effect "
                        "on failures in the middle of computation.\n  %s" % _exception_message(e))
                    warnings.warn(msg)
                    raise

        # Below is toPandas without Arrow optimization.
        pdf = pd.DataFrame.from_records(self.collect(), columns=self.columns)

        dtype = {}
        for field in self.schema:
            pandas_type = _to_corrected_pandas_type(field.dataType)
            # SPARK-21766: if an integer field is nullable and has null values, it can be
            # inferred by pandas as float column. Once we convert the column with NaN back
            # to integer type e.g., np.int16, we will hit exception. So we use the inferred
            # float type, not the corrected type from the schema in this case.
            if pandas_type is not None and \
                not(isinstance(field.dataType, IntegralType) and field.nullable and
                    pdf[field.name].isnull().any()):
                dtype[field.name] = pandas_type

        for f, t in dtype.items():
            pdf[f] = pdf[f].astype(t, copy=False)

        if timezone is None:
            return pdf
        else:
            from pyspark.sql.types import _check_series_convert_timestamps_local_tz
            for field in self.schema:
                # TODO: handle nested timestamps, such as ArrayType(TimestampType())?
                if isinstance(field.dataType, TimestampType):
                    pdf[field.name] = \
                        _check_series_convert_timestamps_local_tz(pdf[field.name], timezone)
            return pdf