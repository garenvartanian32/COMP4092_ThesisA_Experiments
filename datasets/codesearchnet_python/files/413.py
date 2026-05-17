def json(self, path, schema=None, primitivesAsString=None, prefersDecimal=None,
             allowComments=None, allowUnquotedFieldNames=None, allowSingleQuotes=None,
             allowNumericLeadingZero=None, allowBackslashEscapingAnyCharacter=None,
             mode=None, columnNameOfCorruptRecord=None, dateFormat=None, timestampFormat=None,
             multiLine=None, allowUnquotedControlChars=None, lineSep=None, samplingRatio=None,
             dropFieldIfAllNull=None, encoding=None, locale=None):
        """
        Loads JSON files and returns the results as a :class:`DataFrame`.

        `JSON Lines <http://jsonlines.org/>`_ (newline-delimited JSON) is supported by default.
        For JSON (one record per file), set the ``multiLine`` parameter to ``true``.

        If the ``schema`` parameter is not specified, this function goes
        through the input once to determine the input schema.

        :param path: string represents path to the JSON dataset, or a list of paths,
                     or RDD of Strings storing JSON objects.
        :param schema: an optional :class:`pyspark.sql.types.StructType` for the input schema or
                       a DDL-formatted string (For example ``col0 INT, col1 DOUBLE``).
        :param primitivesAsString: infers all primitive values as a string type. If None is set,
                                   it uses the default value, ``false``.
        :param prefersDecimal: infers all floating-point values as a decimal type. If the values
                               do not fit in decimal, then it infers them as doubles. If None is
                               set, it uses the default value, ``false``.
        :param allowComments: ignores Java/C++ style comment in JSON records. If None is set,
                              it uses the default value, ``false``.
        :param allowUnquotedFieldNames: allows unquoted JSON field names. If None is set,
                                        it uses the default value, ``false``.
        :param allowSingleQuotes: allows single quotes in addition to double quotes. If None is
                                        set, it uses the default value, ``true``.
        :param allowNumericLeadingZero: allows leading zeros in numbers (e.g. 00012). If None is
                                        set, it uses the default value, ``false``.
        :param allowBackslashEscapingAnyCharacter: allows accepting quoting of all character
                                                   using backslash quoting mechanism. If None is
                                                   set, it uses the default value, ``false``.
        :param mode: allows a mode for dealing with corrupt records during parsing. If None is
                     set, it uses the default value, ``PERMISSIVE``.

                * ``PERMISSIVE`` : when it meets a corrupted record, puts the malformed string \
                  into a field configured by ``columnNameOfCorruptRecord``, and sets malformed \
                  fields to ``null``. To keep corrupt records, an user can set a string type \
                  field named ``columnNameOfCorruptRecord`` in an user-defined schema. If a \
                  schema does not have the field, it drops corrupt records during parsing. \
                  When inferring a schema, it implicitly adds a ``columnNameOfCorruptRecord`` \
                  field in an output schema.
                *  ``DROPMALFORMED`` : ignores the whole corrupted records.
                *  ``FAILFAST`` : throws an exception when it meets corrupted records.

        :param columnNameOfCorruptRecord: allows renaming the new field having malformed string
                                          created by ``PERMISSIVE`` mode. This overrides
                                          ``spark.sql.columnNameOfCorruptRecord``. If None is set,
                                          it uses the value specified in
                                          ``spark.sql.columnNameOfCorruptRecord``.
        :param dateFormat: sets the string that indicates a date format. Custom date formats
                           follow the formats at ``java.time.format.DateTimeFormatter``. This
                           applies to date type. If None is set, it uses the
                           default value, ``yyyy-MM-dd``.
        :param timestampFormat: sets the string that indicates a timestamp format.
                                Custom date formats follow the formats at
                                ``java.time.format.DateTimeFormatter``.
                                This applies to timestamp type. If None is set, it uses the
                                default value, ``yyyy-MM-dd'T'HH:mm:ss.SSSXXX``.
        :param multiLine: parse one record, which may span multiple lines, per file. If None is
                          set, it uses the default value, ``false``.
        :param allowUnquotedControlChars: allows JSON Strings to contain unquoted control
                                          characters (ASCII characters with value less than 32,
                                          including tab and line feed characters) or not.
        :param encoding: allows to forcibly set one of standard basic or extended encoding for
                         the JSON files. For example UTF-16BE, UTF-32LE. If None is set,
                         the encoding of input JSON will be detected automatically
                         when the multiLine option is set to ``true``.
        :param lineSep: defines the line separator that should be used for parsing. If None is
                        set, it covers all ``\\r``, ``\\r\\n`` and ``\\n``.
        :param samplingRatio: defines fraction of input JSON objects used for schema inferring.
                              If None is set, it uses the default value, ``1.0``.
        :param dropFieldIfAllNull: whether to ignore column of all null values or empty
                                   array/struct during schema inference. If None is set, it
                                   uses the default value, ``false``.
        :param locale: sets a locale as language tag in IETF BCP 47 format. If None is set,
                       it uses the default value, ``en-US``. For instance, ``locale`` is used while
                       parsing dates and timestamps.

        >>> df1 = spark.read.json('python/test_support/sql/people.json')
        >>> df1.dtypes
        [('age', 'bigint'), ('name', 'string')]
        >>> rdd = sc.textFile('python/test_support/sql/people.json')
        >>> df2 = spark.read.json(rdd)
        >>> df2.dtypes
        [('age', 'bigint'), ('name', 'string')]

        """
        self._set_opts(
            schema=schema, primitivesAsString=primitivesAsString, prefersDecimal=prefersDecimal,
            allowComments=allowComments, allowUnquotedFieldNames=allowUnquotedFieldNames,
            allowSingleQuotes=allowSingleQuotes, allowNumericLeadingZero=allowNumericLeadingZero,
            allowBackslashEscapingAnyCharacter=allowBackslashEscapingAnyCharacter,
            mode=mode, columnNameOfCorruptRecord=columnNameOfCorruptRecord, dateFormat=dateFormat,
            timestampFormat=timestampFormat, multiLine=multiLine,
            allowUnquotedControlChars=allowUnquotedControlChars, lineSep=lineSep,
            samplingRatio=samplingRatio, dropFieldIfAllNull=dropFieldIfAllNull, encoding=encoding,
            locale=locale)
        if isinstance(path, basestring):
            path = [path]
        if type(path) == list:
            return self._df(self._jreader.json(self._spark._sc._jvm.PythonUtils.toSeq(path)))
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
            return self._df(self._jreader.json(jrdd))
        else:
            raise TypeError("path can be only string, list or RDD")