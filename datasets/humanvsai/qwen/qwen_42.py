def prod(self, vars_list):

    def prod(self, vars_list):
        """Returns the TensorFluent for the prod aggregation function.

        Args:
            vars_list: The list of variables to be aggregated over.

        Returns:
            A TensorFluent wrapping the prod aggregation function."""
        return self._wrap(tf.reduce_prod(vars_list, axis=0))