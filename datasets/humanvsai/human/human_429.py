def input_size(self):
        shape = self.input_shape
        if shape is None:
            raise util.ConfigurationError(
                'undefined input size for layer "{}"'.format(self.name))
        return shape[-1]