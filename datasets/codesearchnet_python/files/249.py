def sample(self, withReplacement=None, fraction=None, seed=None):
        """Returns a sampled subset of this :class:`DataFrame`.

        :param withReplacement: Sample with replacement or not (default False).
        :param fraction: Fraction of rows to generate, range [0.0, 1.0].
        :param seed: Seed for sampling (default a random seed).

        .. note:: This is not guaranteed to provide exactly the fraction specified of the total
            count of the given :class:`DataFrame`.

        .. note:: `fraction` is required and, `withReplacement` and `seed` are optional.

        >>> df = spark.range(10)
        >>> df.sample(0.5, 3).count()
        7
        >>> df.sample(fraction=0.5, seed=3).count()
        7
        >>> df.sample(withReplacement=True, fraction=0.5, seed=3).count()
        1
        >>> df.sample(1.0).count()
        10
        >>> df.sample(fraction=1.0).count()
        10
        >>> df.sample(False, fraction=1.0).count()
        10
        """

        # For the cases below:
        #   sample(True, 0.5 [, seed])
        #   sample(True, fraction=0.5 [, seed])
        #   sample(withReplacement=False, fraction=0.5 [, seed])
        is_withReplacement_set = \
            type(withReplacement) == bool and isinstance(fraction, float)

        # For the case below:
        #   sample(faction=0.5 [, seed])
        is_withReplacement_omitted_kwargs = \
            withReplacement is None and isinstance(fraction, float)

        # For the case below:
        #   sample(0.5 [, seed])
        is_withReplacement_omitted_args = isinstance(withReplacement, float)

        if not (is_withReplacement_set
                or is_withReplacement_omitted_kwargs
                or is_withReplacement_omitted_args):
            argtypes = [
                str(type(arg)) for arg in [withReplacement, fraction, seed] if arg is not None]
            raise TypeError(
                "withReplacement (optional), fraction (required) and seed (optional)"
                " should be a bool, float and number; however, "
                "got [%s]." % ", ".join(argtypes))

        if is_withReplacement_omitted_args:
            if fraction is not None:
                seed = fraction
            fraction = withReplacement
            withReplacement = None

        seed = long(seed) if seed is not None else None
        args = [arg for arg in [withReplacement, fraction, seed] if arg is not None]
        jdf = self._jdf.sample(*args)
        return DataFrame(jdf, self.sql_ctx)