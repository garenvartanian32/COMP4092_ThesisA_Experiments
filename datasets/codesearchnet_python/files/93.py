def saveAsTextFile(self, path, compressionCodecClass=None):
        """
        Save this RDD as a text file, using string representations of elements.

        @param path: path to text file
        @param compressionCodecClass: (None by default) string i.e.
            "org.apache.hadoop.io.compress.GzipCodec"

        >>> tempFile = NamedTemporaryFile(delete=True)
        >>> tempFile.close()
        >>> sc.parallelize(range(10)).saveAsTextFile(tempFile.name)
        >>> from fileinput import input
        >>> from glob import glob
        >>> ''.join(sorted(input(glob(tempFile.name + "/part-0000*"))))
        '0\\n1\\n2\\n3\\n4\\n5\\n6\\n7\\n8\\n9\\n'

        Empty lines are tolerated when saving to text files.

        >>> tempFile2 = NamedTemporaryFile(delete=True)
        >>> tempFile2.close()
        >>> sc.parallelize(['', 'foo', '', 'bar', '']).saveAsTextFile(tempFile2.name)
        >>> ''.join(sorted(input(glob(tempFile2.name + "/part-0000*"))))
        '\\n\\n\\nbar\\nfoo\\n'

        Using compressionCodecClass

        >>> tempFile3 = NamedTemporaryFile(delete=True)
        >>> tempFile3.close()
        >>> codec = "org.apache.hadoop.io.compress.GzipCodec"
        >>> sc.parallelize(['foo', 'bar']).saveAsTextFile(tempFile3.name, codec)
        >>> from fileinput import input, hook_compressed
        >>> result = sorted(input(glob(tempFile3.name + "/part*.gz"), openhook=hook_compressed))
        >>> b''.join(result).decode('utf-8')
        u'bar\\nfoo\\n'
        """
        def func(split, iterator):
            for x in iterator:
                if not isinstance(x, (unicode, bytes)):
                    x = unicode(x)
                if isinstance(x, unicode):
                    x = x.encode("utf-8")
                yield x
        keyed = self.mapPartitionsWithIndex(func)
        keyed._bypass_serializer = True
        if compressionCodecClass:
            compressionCodec = self.ctx._jvm.java.lang.Class.forName(compressionCodecClass)
            keyed._jrdd.map(self.ctx._jvm.BytesToString()).saveAsTextFile(path, compressionCodec)
        else:
            keyed._jrdd.map(self.ctx._jvm.BytesToString()).saveAsTextFile(path)