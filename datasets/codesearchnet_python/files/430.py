def text(self, path, compression=None, lineSep=None):
        """Saves the content of the DataFrame in a text file at the specified path.
        The text files will be encoded as UTF-8.

        :param path: the path in any Hadoop supported file system
        :param compression: compression codec to use when saving to file. This can be one of the
                            known case-insensitive shorten names (none, bzip2, gzip, lz4,
                            snappy and deflate).
        :param lineSep: defines the line separator that should be used for writing. If None is
                        set, it uses the default value, ``\\n``.

        The DataFrame must have only one column that is of string type.
        Each row becomes a new line in the output file.
        """
        self._set_opts(compression=compression, lineSep=lineSep)
        self._jwrite.text(path)