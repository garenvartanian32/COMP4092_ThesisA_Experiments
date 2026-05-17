def csv(self, path, mode=None, compression=None, sep=None, quote=None, escape=None,
            header=None, nullValue=None, escapeQuotes=None, quoteAll=None, dateFormat=None,
            timestampFormat=None, ignoreLeadingWhiteSpace=None, ignoreTrailingWhiteSpace=None,
            charToEscapeQuoteEscaping=None, encoding=None, emptyValue=None, lineSep=None):
        r"""Saves the content of the :class:`DataFrame` in CSV format at the specified path.

        :param path: the path in any Hadoop supported file system
        :param mode: specifies the behavior of the save operation when data already exists.

            * ``append``: Append contents of this :class:`DataFrame` to existing data.
            * ``overwrite``: Overwrite existing data.
            * ``ignore``: Silently ignore this operation if data already exists.
            * ``error`` or ``errorifexists`` (default case): Throw an exception if data already \
                exists.

        :param compression: compression codec to use when saving to file. This can be one of the
                            known case-insensitive shorten names (none, bzip2, gzip, lz4,
                            snappy and deflate).
        :param sep: sets a single character as a separator for each field and value. If None is
                    set, it uses the default value, ``,``.
        :param quote: sets a single character used for escaping quoted values where the
                      separator can be part of the value. If None is set, it uses the default
                      value, ``"``. If an empty string is set, it uses ``u0000`` (null character).
        :param escape: sets a single character used for escaping quotes inside an already
                       quoted value. If None is set, it uses the default value, ``\``
        :param escapeQuotes: a flag indicating whether values containing quotes should always
                             be enclosed in quotes. If None is set, it uses the default value
                             ``true``, escaping all values containing a quote character.
        :param quoteAll: a flag indicating whether all values should always be enclosed in
                          quotes. If None is set, it uses the default value ``false``,
                          only escaping values containing a quote character.
        :param header: writes the names of columns as the first line. If None is set, it uses
                       the default value, ``false``.
        :param nullValue: sets the string representation of a null value. If None is set, it uses
                          the default value, empty string.
        :param dateFormat: sets the string that indicates a date format. Custom date formats
                           follow the formats at ``java.time.format.DateTimeFormatter``. This
                           applies to date type. If None is set, it uses the
                           default value, ``yyyy-MM-dd``.
        :param timestampFormat: sets the string that indicates a timestamp format.
                                Custom date formats follow the formats at
                                ``java.time.format.DateTimeFormatter``.
                                This applies to timestamp type. If None is set, it uses the
                                default value, ``yyyy-MM-dd'T'HH:mm:ss.SSSXXX``.
        :param ignoreLeadingWhiteSpace: a flag indicating whether or not leading whitespaces from
                                        values being written should be skipped. If None is set, it
                                        uses the default value, ``true``.
        :param ignoreTrailingWhiteSpace: a flag indicating whether or not trailing whitespaces from
                                         values being written should be skipped. If None is set, it
                                         uses the default value, ``true``.
        :param charToEscapeQuoteEscaping: sets a single character used for escaping the escape for
                                          the quote character. If None is set, the default value is
                                          escape character when escape and quote characters are
                                          different, ``\0`` otherwise..
        :param encoding: sets the encoding (charset) of saved csv files. If None is set,
                         the default UTF-8 charset will be used.
        :param emptyValue: sets the string representation of an empty value. If None is set, it uses
                           the default value, ``""``.
        :param lineSep: defines the line separator that should be used for writing. If None is
                        set, it uses the default value, ``\\n``. Maximum length is 1 character.

        >>> df.write.csv(os.path.join(tempfile.mkdtemp(), 'data'))
        """
        self.mode(mode)
        self._set_opts(compression=compression, sep=sep, quote=quote, escape=escape, header=header,
                       nullValue=nullValue, escapeQuotes=escapeQuotes, quoteAll=quoteAll,
                       dateFormat=dateFormat, timestampFormat=timestampFormat,
                       ignoreLeadingWhiteSpace=ignoreLeadingWhiteSpace,
                       ignoreTrailingWhiteSpace=ignoreTrailingWhiteSpace,
                       charToEscapeQuoteEscaping=charToEscapeQuoteEscaping,
                       encoding=encoding, emptyValue=emptyValue, lineSep=lineSep)
        self._jwrite.csv(path)