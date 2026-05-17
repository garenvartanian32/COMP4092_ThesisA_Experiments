def jacobian(self, maps):
        r"""Computes the Jacobian of :math:`y = \mathrm{logit}(x; a,b)`.
        This is:
        .. math::
            \frac{\mathrm{d}y}{\mathrm{d}x} = \frac{b -a}{(x-a)(b-x)},
        where :math:`x \in (a, b)`.
        Parameters
        ----------
        maps : dict or FieldArray
            A dictionary or FieldArray which provides a map between the
            parameter name of the variable to transform and its value(s).
        Returns
        -------
        float
            The value of the jacobian at the given point(s).
        """
        x = maps[self._inputvar]
        # check that x is in bounds
        isin = self._bounds.__contains__(x)
        if isinstance(isin, numpy.ndarray) and not isin.all():
            raise ValueError("one or more values are not in bounds")
        elif not isin:
            raise ValueError("{} is not in bounds".format(x))
        return (self._b - self._a)/((x - self._a)*(self._b - x))