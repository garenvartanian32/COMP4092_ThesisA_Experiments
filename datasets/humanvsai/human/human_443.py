def urlencode(query, doseq=0):
    if hasattr(query, "items"):
        # Remove None parameters from query. Dictionaries are mutable, so we can
        # remove the the items directly. dict.keys() creates a copy of the
        # dictionary keys, making it safe to remove elements from the dictionary
        # while iterating.
        for k in list(query.keys()):
            if query[k] is None:
                del query[k]
        # mapping objects
        query = list(query.items())
    else:
        # Remove None parameters from query. Tuples are immutable, so we have to
        # build a new version that does not contain the elements we want to remove,
        # and replace the original with it.
        query = list(filter((lambda x: x[1] is not None), query))
        # it's a bother at times that strings and string-like objects are
        # sequences...
        try:
            # non-sequence items should not work with len()
            # non-empty strings will fail this
            if len(query) and not isinstance(query[0], tuple):
                raise TypeError
            # zero-length sequences of all types will get here and succeed,
            # but that's a minor nit - since the original implementation
            # allowed empty dicts that type of behavior probably should be
            # preserved for consistency
        except TypeError:
            ty, va, tb = sys.exc_info()
            raise TypeError(
                "not a valid non-string sequence or mapping object"
            ).with_traceback(tb)
    l = []
    if not doseq:
        # preserve old behavior
        for k, v in query:
            k = encodeQueryElement(str(k))
            v = encodeQueryElement(str(v))
            l.append(k + '=' + v)
    else:
        for k, v in query:
            k = encodeQueryElement(str(k))
            if isinstance(v, str):
                v = encodeQueryElement(v)
                l.append(k + '=' + v)
            elif isinstance(v, str):
                # is there a reasonable way to convert to ASCII?
                # encode generates a string, but "replace" or "ignore"
                # lose information and "strict" can raise UnicodeError
                v = encodeQueryElement(v.encode("ASCII", "replace"))
                l.append(k + '=' + v)
            else:
                try:
                    # is this a sufficient test for sequence-ness?
                    len(v)
                except TypeError:
                    # not a sequence
                    v = encodeQueryElement(str(v))
                    l.append(k + '=' + v)
                else:
                    # loop over the sequence
                    for elt in v:
                        l.append(k + '=' + encodeQueryElement(str(elt)))
    return '&'.join(sorted(l))