def csv(self, path, schema=None, sep=None, encoding=None, quote=None, escape=None,
            comment=None, header=None, inferSchema=None, ignoreLeadingWhiteSpace=None,
            ignoreTrailingWhiteSpace=None, nullValue=None, nanValue=None, positiveInf=None,
            negativeInf=None, dateFormat=None, timestampFormat=None, maxColumns=None,
            maxCharsPerColumn=None, maxMalformedLogPerPartition=None, mode=None,
            columnNameOfCorruptRecord=None, multiLine=None, charToEscapeQuoteEscaping=None,
            samplingRatio=None, enforceSchema=None, emptyValue=None, locale=None, lineSep=None):
        r"""Loads a CSV file and returns the result as a  :class:`DataFrame`.

        This function will go through the input once to determine the input schema if
        ``inferSchema`` is enabled. To avoid going through the entire data once, disable
        ``inferSchema`` option or specify the schema explicitly using ``schema``.

        :param path: string, or list of strings, for input path(s),
                     or RDD of Strings storing CSV rows.
        :param schema: an optional :class:`pyspark.sql.types.StructType` for the input schema
                       or a DDL-formatted string (For example ``col0 INT, col1 DOUBLE``).
        :param sep: sets a single character as a separator for each field and value.
                    If None is set, it uses the default value, ``,``.
        :param encoding: decodes the CSV files by the given encoding type. If None is set,
                         it uses the default value, ``UTF-8``.
        :param quote: sets a single character used for escaping quoted values where the
                      separator can be part of the value. If None is set, it uses the default
                      value, ``"``. If you would like to turn off quotations, you need to set an
                      empty string.
        :param escape: sets a single character used for escaping quotes inside an already
                       quoted value. If None is set, it uses the default value, ``\``.
        :param comment: sets a single character used for skipping lines beginning with this
                        character. By default (None), it is disabled.
        :param header: uses the first line as names of columns. If None is set, it uses the
                       default value, ``false``.
        :param inferSchema: infers the input schema automatically from data. It requires one extra
                       pass over the data. If None is set, it uses the default value, ``false``.
        :param enforceSchema: If it is set to ``true``, the specified or inferred schema will be
                              forcibly applied to datasource files, and headers in CSV files will be
                              ignored. If the option is set to ``false``, the schema will be
                              validated against all headers in CSV files or the first header in RDD
                              if the ``header`` option is set to ``true``. Field names in the schema
                              and column names in CSV headers are checked by their positions
                              taking into account ``spark.sql.caseSensitive``. If None is set,
                              ``true`` is used by default. Though the default value is ``true``,
                              it is recommended to disable the ``enforceSchema`` option
                              to avoid incorrect results.
        :param ignoreLeadingWhiteSpace: A flag indicating whether or not leading whitespaces from
                                        values being read should be skipped. If None is set, it
                                        uses the default value, ``false``.
        :param ignoreTrailingWhiteSpace: A flag indicating whether or not trailing whitespaces from
                                         values being read should be skipped. If None is set, it
                                         uses the default value, ``false``.
        :param nullValue: sets the string representation of a null value. If None is set, it uses
                          the default value, empty string. Since 2.0.1, this ``nullValue`` param
                          applies to all supported types including the string type.
        :param nanValue: sets the string representation of a non-number value. If None is set, it
                         uses the default value, ``NaN``.
        :param positiveInf: sets the string representation of a positive infinity value. If None
                            is set, it uses the default value, ``Inf``.
        :param negativeInf: sets the string representation of a negative infinity value. If None
                            is set, it uses the default value, ``Inf``.
        :param dateFormat: sets the string that indicates a date format. Custom date formats
                           follow the formats at ``java.time.format.DateTimeFormatter``. This
                           applies to date type. If None is set, it uses the
                           default value, ``yyyy-MM-dd``.
        :param timestampFormat: sets the string that indicates a timestamp format.
                                Custom date formats follow the formats at
                                ``java.time.format.DateTimeFormatter``.
                                This applies to timestamp type. If None is set, it uses the
                                default value, ``yyyy-MM-dd'T'HH:mm:ss.SSSXXX``.
        :param maxColumns: defines a hard limit of how many columns a record can have. If None is
                           set, it uses the default value, ``20480``.
        :param maxCharsPerColumn: defines the maximum number of characters allowed for any given
                                  value being read. If None is set, it uses the default value,
                                  ``-1`` meaning unlimited length.
        :param maxMalformedLogPerPartition: this parameter is no longer used since Spark 2.2.0.
                                            If specified, it is ignored.
        :param mode: allows a mode for dealing with corrupt records during parsing. If None is
                     set, it uses the default value, ``PERMISSIVE``.

                * ``PERMISSIVE`` : when it meets a corrupted record, puts the malformed string \
                  into a field configured by ``columnNameOfCorruptRecord``, and sets malformed \
                  fields to ``null``. To keep corrupt records, an user can set a string type \
                  field named ``columnNameOfCorruptRecord`` in an user-defined schema. If a \
                  schema does not have the field, it drops corrupt records during parsing. \
                  A record with less/more tokens than schema is not a corrupted record to CSV. \
                  When it meets a record having fewer tokens than the length of the schema, \
                  sets ``null`` to extra fields. When the record has more tokens than the \
                  length of the schema, it drops extra tokens.
                * ``DROPMALFORMED`` : ignores the whole corrupted records.
                * ``FAILFAST`` : throws an exception when it meets corrupted records.

        :param columnNameOfCorruptRecord: allows renaming the new field having malformed string
                                          created by ``PERMISSIVE`` mode. This overrides
                                          ``spark.sql.columnNameOfCorruptRecord``. If None is set,
                                          it uses the value specified in
                                          ``spark.sql.columnNameOfCorruptRecord``.
        :param multiLine: parse records, which may span multiple lines. If None is
                          set, it uses the default value, ``false``.
        :param charToEscapeQuoteEscaping: sets a single character used for escaping the escape for
                                          the quote character. If None is set, the default value is
                                          escape character when escape and quote characters are
                                          different, ``\0`` otherwise.
        :param samplingRatio: defines fraction of rows used for schema inferring.
                              If None is set, it uses the default value, ``1.0``.
        :param emptyValue: sets the string representation of an empty value. If None is set, it uses
                           the default value, empty string.
        :param locale: sets a locale as language tag in IETF BCP 47 format. If None is set,
                       it uses the default value, ``en-US``. For instance, ``locale`` is used while
                       parsing dates and timestamps.
        :param lineSep: defines the line separator that should be used for parsing. If None is
                        set, it covers all ``\\r``, ``\\r\\n`` and ``\\n``.
                        Maximum length is 1 character.

        >>> df = spark.read.csv('python/test_support/sql/ages.csv')
        >>> df.dtypes
        [('_c0', 'string'), ('_c1', 'string')]
        >>> rdd = sc.textFile('python/test_support/sql/ages.csv')
        >>> df2 = spark.read.csv(rdd)
        >>> df2.dtypes
        [('_c0', 'string'), ('_c1', 'string')]
        """
        self._set_opts(
            schema=schema, sep=sep, encoding=encoding, quote=quote, escape=escape, comment=comment,
            header=header, inferSchema=inferSchema, ignoreLeadingWhiteSpace=ignoreLeadingWhiteSpace,
            ignoreTrailingWhiteSpace=ignoreTrailingWhiteSpace, nullValue=nullValue,
            nanValue=nanValue, positiveInf=positiveInf, negativeInf=negativeInf,
            dateFormat=dateFormat, timestampFormat=timestampFormat, maxColumns=maxColumns,
            maxCharsPerColumn=maxCharsPerColumn,
            maxMalformedLogPerPartition=maxMalformedLogPerPartition, mode=mode,
            columnNameOfCorruptRecord=columnNameOfCorruptRecord, multiLine=multiLine,
            charToEscapeQuoteEscaping=charToEscapeQuoteEscaping, samplingRatio=samplingRatio,
            enforceSchema=enforceSchema, emptyValue=emptyValue, locale=locale, lineSep=lineSep)
        if isinstance(path, basestring):
            path = [path]
        if type(path) == list:
            return self._df(self._jreader.csv(self._spark._sc._jvm.PythonUtils.toSeq(path)))
        elif isinstance(path, RDD):
            def func(iterator):
                for x in iterator:
                    if not isinstance(x, basestring):
                        x = unicode(x)
                    if isinstance(x, unicode):
                        x = x.encode("utf-8")
                    yield x
            keyed = path.mapPartitions(func)
            keyed._bypass_serializer = True
            jrdd = keyed._jrdd.map(self._spark._jvm.BytesToString())
            # see SPARK-22112
            # There aren't any jvm api for creating a dataframe from rdd storing csv.
            # We can do it through creating a jvm dataset firstly and using the jvm api
            # for creating a dataframe from dataset storing csv.
            jdataset = self._spark._ssql_ctx.createDataset(
                jrdd.rdd(),
                self._spark._jvm.Encoders.STRING())
            return self._df(self._jreader.csv(jdataset))
        else:
            raise TypeError("path can be only string, list or RDD")