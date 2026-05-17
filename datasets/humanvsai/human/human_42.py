def prod(self, vars_list: List[str]) -> 'TensorFluent':
        operand = self
        if operand.dtype == tf.bool:
            operand = operand.cast(tf.float32)
        return self._aggregation_op(tf.reduce_prod, operand, vars_list)